using System;
using System.Drawing;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Andersc.CodePlay.PlayForms
{
    public partial class MainForm : Form
    {
        private CancellationTokenSource cancelToken = new CancellationTokenSource();

        public MainForm()
        {
            InitializeComponent();
        }

        private void btnProcess_Click(object sender, System.EventArgs e)
        {
            Task.Factory.StartNew(ProcessFiles);
        }

        private void ProcessFiles()
        {
            // Store the CancellationToken
            var parOptions = new ParallelOptions();
            parOptions.CancellationToken = cancelToken.Token;
            parOptions.MaxDegreeOfParallelism = System.Environment.ProcessorCount;
            parOptions.MaxDegreeOfParallelism = 2;

            var files = Directory.GetFiles(@"C:\andersc\pics", "*.jpg", SearchOption.AllDirectories);
            var newDir = @"C:\andersc\modified";
            Directory.CreateDirectory(newDir);

            try
            {
                Parallel.ForEach(files, parOptions, file =>
                {
                    parOptions.CancellationToken.ThrowIfCancellationRequested();

                    var fName = Path.GetFileName(file);
                    using (var bitmap = new Bitmap(file))
                    {
                        bitmap.RotateFlip(RotateFlipType.Rotate180FlipNone);
                        bitmap.Save(Path.Combine(newDir, fName));

                        //this.Text = string.Format("Processing {0} on thread {1}", fName,
                        //    Thread.CurrentThread.ManagedThreadId);
                        this.Invoke((Action)delegate
                        {
                            this.Text = string.Format("Processing {0} on thread {1}", file,
                                Thread.CurrentThread.ManagedThreadId);
                        });

                        Thread.Sleep(200);
                    }
                });

                this.Invoke((Action)delegate
                {
                    this.Text = "Done!";
                });
            }
            catch (OperationCanceledException ex)
            {
                this.Invoke((Action) delegate
                {
                    this.Text = ex.Message;
                });
            }
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            // Tell all the worker threads to stop.
            cancelToken.Cancel();
        }
    }
}
