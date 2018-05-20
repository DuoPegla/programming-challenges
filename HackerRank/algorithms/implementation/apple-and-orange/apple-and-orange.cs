using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution {

    // Complete the countApplesAndOranges function below.
    static void countApplesAndOranges(int s, int t, int a, int b, int[] apples, int[] oranges) 
    {
        int appleCount = 0;
        foreach (int apple in apples)
        {
            int appleLocation = a + apple;
            if (appleLocation >= s && appleLocation <= t)
                appleCount++;
        }
        
        int orangeCount = 0;
        foreach (int orange in oranges)
        {
            int orangeLocation = b + orange;
            if (orangeLocation >= s && orangeLocation <= t)
                orangeCount++;
        }
        
        Console.WriteLine(appleCount);
        Console.WriteLine(orangeCount);
    }

    static void Main(string[] args) {
        string[] st = Console.ReadLine().Split(' ');

        int s = Convert.ToInt32(st[0]);

        int t = Convert.ToInt32(st[1]);

        string[] ab = Console.ReadLine().Split(' ');

        int a = Convert.ToInt32(ab[0]);

        int b = Convert.ToInt32(ab[1]);

        string[] mn = Console.ReadLine().Split(' ');

        int m = Convert.ToInt32(mn[0]);

        int n = Convert.ToInt32(mn[1]);

        int[] apple = Array.ConvertAll(Console.ReadLine().Split(' '), appleTemp => Convert.ToInt32(appleTemp))
        ;

        int[] orange = Array.ConvertAll(Console.ReadLine().Split(' '), orangeTemp => Convert.ToInt32(orangeTemp))
        ;
        countApplesAndOranges(s, t, a, b, apple, orange);
    }
}
