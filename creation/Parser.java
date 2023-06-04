import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.List;
import java.util.stream.Stream;

public class Parser {

  public static String pathname = "/Users/main/Enigmaths/Enigmaths/creation/";

  public static void main(String[] args) {
    System.out.println("Hello world");

    String fileInname = "input.txt";

    // Try to read file into Stream
    try (Stream<String> stream = Files.lines(Paths.get(pathname + fileInname))) {
      List<String> sphenics = stream.map(t -> t.substring(t.indexOf(' ') + 1)).toList();
      List<String> three = sphenics.stream().filter(t -> (t.length() == 3)).toList();// fix this to filter by length
      System.out.println("Three:" + three.toString());

      List<String> four = sphenics.stream().filter(t -> (t.length() == 4)).toList();
      System.out.println("Four:" + four.toString());

      listToFile("three_dig_sphenics.txt", three);
      listToFile("four_dig_sphenics.txt", four);
    } catch (IOException e) {
      e.printStackTrace();
    }

  }

  private static void listToFile(String filename, List<String> list) throws IOException {

    Files.deleteIfExists(Paths.get(pathname + filename));
    Files.createFile(Paths.get(pathname + filename));
    for (String str : list) {
      Files.writeString(Paths.get(pathname + filename), str + System.lineSeparator(), StandardOpenOption.APPEND);
    }
  }
}