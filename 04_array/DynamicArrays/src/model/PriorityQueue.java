package model;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;


public class PriorityQueue<T> {
    private final List<Queue<T>> priorities;
    private final int maxPriority;

    public PriorityQueue(Integer maxPriorityAllowed) {
        maxPriority = maxPriorityAllowed;
        priorities = Stream.generate(Queue<T>::new)
                .limit(maxPriority)
                .collect(Collectors.toList());
    }

    public void enqueue(T item, int priority) {
        priorities.get(priority).enqueue(item);
    }

    public T dequeue() {
        for (int i = 0; i < maxPriority; ++i) {
            if (!priorities.get(i).isEmpty()) {
                return priorities.get(i).dequeue();
            }
        }
        return null;
    }
}
