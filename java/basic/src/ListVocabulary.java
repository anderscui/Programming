import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class ListVocabulary implements Vocabulary {

    private List<String> words = new ArrayList<String>();

    public ListVocabulary(Collection<String> words) {
        this.words.addAll(words);
        Collections.sort(this.words);
    }

    @Override
    public boolean add(String word) {
        int pos = Collections.binarySearch(words, word);
        if(pos < 0) {
            words.add(-(pos+1), word);
            return true;
        }
        return false;
    }

    @Override
    public boolean isPrefix(String prefix) {
        int pos = Collections.binarySearch(words, prefix);
        if (pos >= 0) {
            // the prefix is a word
            if (pos < words.size() - 1) {
                String next = words.get(pos+1);
                return next.startsWith(prefix);
            }
            return false;
        }

        pos = -(pos+1);
        if (pos == words.size()) {
            return false;
        }

        String next = words.get(pos);
        return next.startsWith(prefix);
    }

    @Override
    public boolean contains(String word) {
        return Collections.binarySearch(words, word) >= 0;
    }
}
