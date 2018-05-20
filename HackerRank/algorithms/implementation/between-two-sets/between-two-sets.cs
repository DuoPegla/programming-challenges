using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    /*
     * Complete the getTotalX function below.
     */
    static int getTotalX(int[] a, int[] b) {
        /*
         * Write your code here.
         */
        List<int> sortedA = new List<int>(a);
        sortedA.Sort();
        
        List<int> sortedB = new List<int>(b);
        sortedB.Sort();
        
        int count = 0;
        for (int i = sortedA[sortedA.Count-1]; i <= sortedB[0]; i++)
        {
            if (areElementsFactors(sortedA.ToArray(), i) && isNumberFactor(sortedB.ToArray(), i))
                count++;
        }
        
        return count;
    }
    
    static bool areElementsFactors(int[] a, int n)
    {
        foreach (int i in a)
        {
            if (n%i != 0)
                return false;
        }
        
        return true;
    }
    
    static bool isNumberFactor(int[] a, int n)
    {
        foreach (int i in a)
        {
            if (i%n != 0)
                return false;
        }
        return true;
    }

    static void Main(string[] args) {
        TextWriter tw = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string[] nm = Console.ReadLine().Split(' ');

        int n = Convert.ToInt32(nm[0]);

        int m = Convert.ToInt32(nm[1]);

        int[] a = Array.ConvertAll(Console.ReadLine().Split(' '), aTemp => Convert.ToInt32(aTemp))
        ;

        int[] b = Array.ConvertAll(Console.ReadLine().Split(' '), bTemp => Convert.ToInt32(bTemp))
        ;
        int total = getTotalX(a, b);

        tw.WriteLine(total);

        tw.Flush();
        tw.Close();
    }
}
