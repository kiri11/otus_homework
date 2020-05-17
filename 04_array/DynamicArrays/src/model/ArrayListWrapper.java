package model;

import java.util.ArrayList;

public class ArrayListWrapper<T> implements IArray<T> {

    private final ArrayList<T> array;

    public ArrayListWrapper() {
        array = new ArrayList<T>();
    }

    @Override
    public int size() {
        return array.size();
    }

    @Override
    public void add(T item) {
        add(item, size());
    }

    @Override
    public void add(T item, int index) {
        array.add(index, item);
    }

    @Override
    public T get(int index) {
        return array.get(index);
    }

    @Override
    public T remove(int index){
        return array.remove(index);
    }

}
