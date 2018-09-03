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

    // Complete the dayOfProgrammer function below.
    static string dayOfProgrammer(int year) 
    {
        int remainingDays = 256;
        int month = 1;
        
        // Transition year
        if (year == 1918)
        {
            while (remainingDays > 0)
            {
                int daysInMonth;
                if (month == 2)
                {
                    daysInMonth = 15;
                }
                else
                {
                    daysInMonth = DateTime.DaysInMonth(year, month);
                }

                if (remainingDays - daysInMonth <= 0)
                {
                    break;
                }

                month++;
                remainingDays -= daysInMonth;
            }
        }
        else
        {
            while (remainingDays > 0)
            {
                int daysInMonth;
                if (month == 2)
                {
                    if (IsLeapYear(year))
                        daysInMonth = 29;
                    else
                        daysInMonth = 28;
                }
                else
                {
                    daysInMonth = DateTime.DaysInMonth(year, month);
                }
                
                if (remainingDays - daysInMonth <= 0)
                {
                    break;
                }
                
                month++;
                remainingDays -= daysInMonth;
            }
        }
        
        string result = remainingDays.ToString("00") + "." + month.ToString("00") + "." + year;
        Console.WriteLine(result);
        return result;
        
    } 
    
    static bool IsLeapYear(int year)
    {
        if (year < 1918)
        {
            return year % 4 == 0;
        }
        else
        {
            return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
        }
    }

    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int year = Convert.ToInt32(Console.ReadLine().Trim());

        string result = dayOfProgrammer(year);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
