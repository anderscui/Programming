import org.apache.poi.xwpf.converter.core.BasicURIResolver;
import org.apache.poi.xwpf.converter.core.FileImageExtractor;
import org.apache.poi.xwpf.converter.core.FileURIResolver;
import org.apache.poi.xwpf.converter.xhtml.XHTMLConverter;
import org.apache.poi.xwpf.converter.xhtml.XHTMLOptions;
import org.apache.poi.xwpf.usermodel.XWPFDocument;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.TransformerException;
import java.io.*;
import java.nio.file.Paths;

public class converter {
    public static void main(String[] args) throws IOException, TransformerException, ParserConfigurationException {
//        System.out.println("hello");
        // convertDocx();
//        System.out.println(getDocxContent("/Users/andersc/data/resumes/test/doc/胡长山.doc",
//                "/Users/andersc/data/resumes/test/doc/image"));

        // docx2Html("/Users/andersc/data/resumes/test/doc/胡长山.docx", "/Users/andersc/data/resumes/test/doc/胡s.html");
        docx2Html("/Users/andersc/data/resumes/test/doc/姚伟.docx", "/Users/andersc/data/resumes/test/doc/姚伟.html");
    }

    private static String getDocxContent(String docFilePath, String picDir) throws IOException {
        File docFile = new File(docFilePath);
        String docDir = docFile.getParent();

        final String picPath = Paths.get(docDir, picDir).toString();

        InputStream in = new FileInputStream(docFile);
        XWPFDocument document = new XWPFDocument(in);

        XHTMLOptions options = XHTMLOptions.create();
        options.setExtractor(new FileImageExtractor(new File(picDir)));
        options.URIResolver(new BasicURIResolver("image"));

        OutputStream baos = new ByteArrayOutputStream() ;

//        OutputStreamWriter outputStreamWriter = new OutputStreamWriter(new FileOutputStream("test.html"),
//                StandardCharsets.UTF_8);
        XHTMLConverter.getInstance().convert(document, baos, options);
        baos.close();
        String content = baos.toString();
        System.out.println(content);

        return content;
    }

    private static void convertDocx() throws IOException {
        String sourceFileName = "/Users/andersc/data/resumes/test/doc/胡长山.doc";
        String targetFileName = "/Users/andersc/data/resumes/test/doc/胡长山22.html";
        String imagePathStr = "/Users/andersc/data/resumes/test/doc/image";

        OutputStreamWriter outputStreamWriter = null;

        try {
            XWPFDocument document = new XWPFDocument(new FileInputStream(sourceFileName));
            XHTMLOptions options = XHTMLOptions.create();
            // 存放图片的文件夹
            options.setExtractor(new FileImageExtractor(new File(imagePathStr)));
            // html中图片的路径
            options.URIResolver(new BasicURIResolver("image"));
            outputStreamWriter = new OutputStreamWriter(new FileOutputStream(targetFileName), "utf-8");
            XHTMLConverter xhtmlConverter = (XHTMLConverter) XHTMLConverter.getInstance();
            xhtmlConverter.convert(document, outputStreamWriter, options);
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (outputStreamWriter != null) {
                outputStreamWriter.close();
            }
        }
    }

    public static void docx2Html(String fileName, String outPutFile) throws TransformerException, IOException, ParserConfigurationException {
        long startTime = System.currentTimeMillis();

        String fileOutName = outPutFile;
        XWPFDocument document = new XWPFDocument(new FileInputStream(fileName));
        XHTMLOptions options = XHTMLOptions.create().indent(4);
        // 导出图片
        File imageFolder = new File("/Users/andersc/images");
        options.setExtractor(new FileImageExtractor(imageFolder));
        // URI resolver
        options.URIResolver(new FileURIResolver(imageFolder));
        File outFile = new File(fileOutName);
        outFile.getParentFile().mkdirs();
        OutputStream out = new FileOutputStream(outFile);
        XHTMLConverter.getInstance().convert(document, out, options);

        System.out.println("Generate " + fileOutName + " with " + (System.currentTimeMillis() - startTime) + " ms.");
    }
}
