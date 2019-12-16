package tour.java.io;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

public class inputStream {
    public static void main(String[] args) throws IOException {
        String homePage = "https://cn.bing.com/";
        URL url = new URL(homePage);
        InputStream ins = url.openStream();
        char b = (char)ins.read();
        System.out.println(b);
    }
}
