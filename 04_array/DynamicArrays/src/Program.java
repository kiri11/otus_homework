import model.*;

import java.util.Date;

public class Program {

    public static void main(String[] args) {
        IArray singleArray = new SingleArray();
        IArray vectorArray = new VectorArray();
        IArray factorArray = new FactorArray();
        IArray matrixArray = new MatrixArray();
        IArray builtinArray = new ArrayListWrapper();
        int N = 100_000;
        testAddArray(singleArray, N);
        testAddArray(vectorArray, N);
        testAddArray(factorArray, N);
        testAddArray(matrixArray, N);
        testAddArray(builtinArray, N);
    }

    private static void testAddArray(IArray data, int total) {
        long start = System.currentTimeMillis();

        for (int j = 0; j < total; j ++)
            data.add(new Date());

        System.out.println(data + " testAddArray: " +
                (System.currentTimeMillis() - start));
    }
}
