package model;

public class MatrixArray<T> implements IArray<T> {

    private int size;
    private final int step;
    private final IArray<IArray<T>> array;

    public MatrixArray(int step) {
        this.step = step;
        array = new FactorArray<>();
        size = 0;
    }

    public MatrixArray() {
        this(10);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void add(T item, int index) {
        FactorArray<T> temp = new FactorArray<>();
        if (index / step < array.size() - 1) {
            for (int i = index; i < size; ++i) {
                temp.add(get(i));
            }
            while (index / step < array.size() - 1) {
                array.remove(array.size()-1);
            }
        } else if (size == array.size() * step) {
            array.add(new VectorArray<T>(step));
        }

        // Last VectorArray
        int last_index = index - (array.size() - 1) * step;
        array.get(array.size() - 1).add(item, last_index);
        for (int i = index+1; i < size; ++i) {
            add(temp.get(i));
        }

        size++;
    }

    @Override
    public void add(T item) {
        add(item, size());
    }

    @Override
    public T remove(int index) {
        T removed = get(index);
        if (index / step < array.size() - 1) {
            FactorArray<T> temp = new FactorArray<>();
            for (int i = index; i < size; ++i) {
                temp.add(get(i));
            }
            while (index / step < array.size() - 1) {
                array.remove(array.size() - 1);
            }
            for (int i = index-1; i < size; ++i) {
                add(temp.get(i));
            }
        } else {
            array.get(array.size() - 1).remove(index - (array.size() - 1) * step);
        }
        --size;
        return removed;
    }

    @Override
    public T get(int index) {
        return array.get(index / step).get(index % step);
    }
}
