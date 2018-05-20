using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    /*
     * Complete the gradingStudents function below.
     */
    static int[] gradingStudents(int[] grades) {
        /*
         * Write your code here.
         */
        List<int> roundedGrades = new List<int>();
        for (int i = 0; i < grades.Count(); i++)
        {
            int remainder = grades[i] % 5;
            if (remainder >= 3 && grades[i] + (5 - remainder) >= 40)
            {
                roundedGrades.Add(grades[i] + (5 - remainder));
            }      
            else
            {
                roundedGrades.Add(grades[i]);
            }
        }
        
        return roundedGrades.ToArray();
    }

    static void Main(string[] args) {
        TextWriter tw = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        int[] grades = new int [n];

        for (int gradesItr = 0; gradesItr < n; gradesItr++) {
            int gradesItem = Convert.ToInt32(Console.ReadLine());
            grades[gradesItr] = gradesItem;
        }

        int[] result = gradingStudents(grades);

        tw.WriteLine(string.Join("\n", result));

        tw.Flush();
        tw.Close();
    }
}
