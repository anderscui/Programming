import java.util.Collection;
import java.util.Set;
import java.util.TreeSet;

/**
 * Created by andersc on 8/20/15.
 */
public class TreeVocabulary extends TreeSet<String> implements Vocabulary {

    public TreeVocabulary(Collection<String> c) {
        super(c);
    }

    @Override
    public boolean isPrefix(String prefix) {
        String next = ceiling(prefix);
        if (next == null) {
            return false;
        }

        if (next.equals(prefix)) {
            Set<String> tail = tailSet(next, false);
            if (tail.isEmpty()) {
                return false;
            }
            next = tail.iterator().next();
        }

        return next.startsWith(prefix);
    }

    @Override
    public boolean contains(String word) {
        return super.contains(word);
    }
}
