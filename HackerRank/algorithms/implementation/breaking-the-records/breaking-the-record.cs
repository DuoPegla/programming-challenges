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

    // Complete the breakingRecords function below.
    static int[] breakingRecords(int[] scores) 
    {
        int lowestScore = scores[0];
        int lowestScoreRecord = 0;
        int highestScore = scores[0];
        int highestScoreRecord = 0;
        for (int i = 1; i < scores.Count(); i++)
        {
            if (scores[i] > highestScore)
            {
                highestScore = scores[i];
                highestScoreRecord++;
            }
            
            if (scores[i] < lowestScore)
            {
                lowestScore = scores[i];
                lowestScoreRecord++;
            }
        }
        
        return new int[] {highestScoreRecord, lowestScoreRecord};
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        int[] score = Array.ConvertAll(Console.ReadLine().Split(' '), scoreTemp => Convert.ToInt32(scoreTemp))
        ;
        int[] result = breakingRecords(score);

        textWriter.WriteLine(string.Join(" ", result));

        textWriter.Flush();
        textWriter.Close();
    }
}
