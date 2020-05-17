package model;

public class SingleArray<T> implements IArray<T> {

    private Object[] array;

    public SingleArray () {
        array = new Object[0];
    }

    @Override
    public int size() {
        return array.length;
    }

    @Override
    public void add(T item) {
        add(item, size());
    }

    @Override
    public void add(T item, int index) {
        Object[] newArray = new Object[size() + 1];
        System.arraycopy(array, 0, newArray, 0, index);
        System.arraycopy(array, index, newArray, index+1, size()-index);
        newArray[index] = item;
        array = newArray;
    }

    @Override
    @SuppressWarnings("unchecked")
    public T get(int index) {
        return (T)array[index];
    }

    @Override
    public T remove(int index){
        Object[] newArray = new Object[size() - 1];
        T res = get(index);
        System.arraycopy(array, 0, newArray, 0, index);
        System.arraycopy(array, index, newArray, index+1, size()-index-1);
        array = newArray;
        return res;
    }

}
