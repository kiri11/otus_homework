package model;

public class FactorArray<T> implements IArray<T> {

    private Object[] array;
    private final int factor;
    private int size;

    public FactorArray(int factor, int initLength) {
        this.factor = factor;
        array = new Object[initLength];
        size = 0;
    }

    public FactorArray() {
        this(2, 10);
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
            Object[] newArray = new Object[array.length + array.length * factor];
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
