import model.*;

import java.util.Date;

public class ProgramPQ {

    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(10);
        int N = 1000;
        testAddPQ(pq, N);
    }

    private static void testAddPQ(PriorityQueue<Integer> data, int total) {
        long start = System.currentTimeMillis();

        for (int j = 0; j < 10; j ++)
            data.enqueue(j, j % 3);

        for (int j = 0; j < 10; j ++)
            System.out.println(data.dequeue());
        System.out.println(data + " testAddPQ: " +
                (System.currentTimeMillis() - start));
    }
}
