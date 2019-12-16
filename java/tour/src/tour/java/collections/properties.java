package tour.java.collections;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Properties;

public class properties {
    public static void main(String[] args) {
        Properties settings = new Properties();
        settings.put("width", "200");
        settings.put("title", "Hello, World");
        try (OutputStream out = Files.newOutputStream(Paths.get("config.properties"))) {
            settings.store(out, "Program Properties");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // list system properties.
        Properties sysProps = System.getProperties();
        for (String prop: sysProps.stringPropertyNames()) {
            System.out.printf("%s: %s \n", prop, sysProps.getProperty(prop));
        }
    }
}
