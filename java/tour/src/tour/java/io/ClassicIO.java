package tour.java.io;

import java.io.*;

public class ClassicIO {
    public static void main(String[] args) throws IOException {
        basicFileIO();
        fileStreams();
    }

    private static void fileStreams() {
        File home = new File(System.getProperty("user.home"));
        File config = new File(home, ".zshrc");
        try (InputStream ins = new FileInputStream(config)) {
            byte[] buf = new byte[4096];
            int len, count = 0;
            while ((len = ins.read(buf)) > 0) {
                for (int i = 0; i < len; i++) {
                    if (buf[i] == 97)
                        count++;
                }
            }
            System.out.println("'a's seen: " + count);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void basicFileIO() {
        File home = new File(System.getProperty("user.home"));
        System.out.println(home);
        File conf = new File(home, "app.conf");
        System.out.println(conf.getAbsoluteFile());
        if (conf.exists() && conf.isFile() && conf.canRead()) {
            File configDir = new File(home, ".configdir");
            configDir.mkdir();
            conf.renameTo(new File(configDir, ".config"));
        }
    }
}
