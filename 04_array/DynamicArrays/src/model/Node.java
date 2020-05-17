package model;

public class Node <T> {
    public T item;
    public Node<T> next;

    Node(T item) {
        this(item, null);
    }

    Node(T item, Node<T> next) {
        this.item = item;
        this.next = next;
    }
}
