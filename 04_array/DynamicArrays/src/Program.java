import model.*;

import java.util.Date;

public class Program {

    public static void main(String[] args) {
        IArray singleArray = new SingleArray();
        IArray vectorArray = new VectorArray();
        IArray factorArray = new FactorArray();
        IArray matrixArray = new MatrixArray();
        IArray builtinArray = new ArrayListWrapper();
        testAddArray(singleArray, 100_000);
        testAddArray(vectorArray, 100_000);
        testAddArray(factorArray, 100_000);
        testAddArray(matrixArray, 100_000);
        testAddArray(builtinArray, 100_000);
    }

    private static void testAddArray(IArray data, int total) {
        long start = System.currentTimeMillis();

        for (int j = 0; j < total; j ++)
            data.add(new Date());

        System.out.println(data + " testAddArray: " +
                (System.currentTimeMillis() - start));
    }
}
