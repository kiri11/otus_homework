package model;

public class VectorArray<T> implements IArray<T> {

    private Object[] array;
    private final int step;
    private int size;

    public VectorArray(int step) {
        this.step = step;
        array = new Object[0];
        size = 0;
    }

    public VectorArray() {
        this(10);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void add(T item) {
        add(item, size());
    }

    @Override
    public void add(T item, int index) {
        if (size() == array.length) {
            Object[] newArray = new Object[size() + step];
            System.arraycopy(array, 0, newArray, 0, index);
            System.arraycopy(array, index, newArray, index + 1, size() - index);
            array = newArray;
        }
        array[index] = item;
        size++;
    }

    @Override
    public T remove(int index) {
        T res = get(index);
        System.arraycopy(array, index, array, index - 1, size() - index -1);
        size--;
        return res;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T)array[index];
    }

}
