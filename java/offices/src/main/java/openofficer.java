import org.jodconverter.DocumentConverter;
import org.jodconverter.JodConverter;
import org.jodconverter.OnlineConverter;
import org.jodconverter.document.DefaultDocumentFormatRegistry;
import org.jodconverter.document.DocumentFormatRegistry;
import org.jodconverter.job.ConversionJobWithOptionalSourceFormatUnspecified;
import org.jodconverter.job.ConversionJobWithRequiredSourceFormatUnspecified;
import org.jodconverter.office.LocalOfficeManager;
import org.jodconverter.office.OfficeException;
import org.jodconverter.office.OfficeUtils;
import org.jodconverter.office.OnlineOfficeManager;

import javax.annotation.Resource;
import java.io.File;
import java.io.InputStream;

public class openofficer {

    @Resource
    private static DocumentConverter documentConverter;

    public static void main(String[] args) throws OfficeException {
        //File input = new File("/Users/andersc/data/resumes/test/doc/岑江简历.doc");
        File input = new File("/Users/andersc/data/resumes/test/doc/王先生_化工英才网20170811_12210419405615.doc");
        File output = new File("/Users/andersc/王先生_化工英才网20170811_12210419405615.pdf");
        final LocalOfficeManager officeManager = LocalOfficeManager.install();
        final OnlineOfficeManager onlineOfficeManager = OnlineOfficeManager
                .builder()
                .urlConnection("https://localhost:9980")
                .build();

        try {
            // officeManager.start();
            onlineOfficeManager.start();
            // OnlineConverter.
            JodConverter.convert(input).as(DefaultDocumentFormatRegistry.HTML)
                    .to(output).as(DefaultDocumentFormatRegistry.PDF)
                    .execute();
        } finally {
            //OfficeUtils.stopQuietly(officeManager);
        }
    }
}
