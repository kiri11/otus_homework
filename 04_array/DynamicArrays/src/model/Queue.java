package model;

public class Queue<T> {
    private Node<T> head, tail;

    public Queue() {
        head = tail = null;
    }

    public Node<T> getHead() {
        return head;
    }

    public boolean isEmpty() {
        return head == null;
    }

    public void enqueue(T item) {
        Node<T> node = new Node<T>(item);
        if (isEmpty()){
            head = tail = node;
        }
        else {
            tail.next = node;
            tail = node;
        }
    }

    public T dequeue() {
        if (!isEmpty()) {
            T item = head.item;
            head = head.next;
            return item;
        } else {
            return null;
        }
    }
}
