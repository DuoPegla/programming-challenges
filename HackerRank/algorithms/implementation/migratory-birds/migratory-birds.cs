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

    // Complete the migratoryBirds function below.
    static int migratoryBirds(int[] ar) 
    {
        Dictionary<int, int> birdSightings = new Dictionary<int, int>();
        int maxSightings = 0;
        int mostCommonId = 0;
        foreach (int i in ar)
        {
            if (birdSightings.ContainsKey(i))
                birdSightings[i]++;
            else
                birdSightings[i] = 1;
            
            if (birdSightings[i] > maxSightings)
            {
                mostCommonId = i;
                maxSightings = birdSightings[i];
            }
            else if (birdSightings[i] == maxSightings && i < mostCommonId)
            {
                mostCommonId = i;
                maxSightings = birdSightings[i];
            }
        }
        
        return mostCommonId;
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int arCount = Convert.ToInt32(Console.ReadLine());

        int[] ar = Array.ConvertAll(Console.ReadLine().Split(' '), arTemp => Convert.ToInt32(arTemp))
        ;
        int result = migratoryBirds(ar);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
