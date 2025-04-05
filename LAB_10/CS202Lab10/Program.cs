// // // // // using System;

// // // // // class Program
// // // // // {
// // // // //     static void Main()
// // // // //     {
// // // // //         Console.WriteLine("Hello, CS202 Lab in VS Code!");
// // // // //     }
// // // // // }


// // // // using System;

// // // // class Calculator
// // // // {
// // // //     static void Main()
// // // //     {
// // // //         Console.Write("Enter first number: ");
// // // //         double num1 = Convert.ToDouble(Console.ReadLine());

// // // //         Console.Write("Enter second number: ");
// // // //         double num2 = Convert.ToDouble(Console.ReadLine());

// // // //         Console.WriteLine($"Addition: {num1 + num2}");
// // // //         Console.WriteLine($"Subtraction: {num1 - num2}");
// // // //         Console.WriteLine($"Multiplication: {num1 * num2}");

// // // //         if (num2 != 0)
// // // //             Console.WriteLine($"Division: {num1 / num2}");
// // // //         else
// // // //             Console.WriteLine("Cannot divide by zero!");

// // // //         Console.WriteLine((num1 + num2) % 2 == 0 ? "Sum is even" : "Sum is odd");
// // // //     }
// // // // }


// // // using System;

// // // class LoopsDemo
// // // {
// // //     static void Main()
// // //     {
// // //         // For Loop
// // //         for (int i = 1; i <= 10; i++)
// // //         {
// // //             Console.Write(i + " ");
// // //         }
// // //         Console.WriteLine();

// // //         // While Loop
// // //         string input;
// // //         do
// // //         {
// // //             Console.Write("Enter a number (or type 'exit' to quit): ");
// // //             input = Console.ReadLine();
// // //         } while (input.ToLower() != "exit");

// // //         // Factorial Function
// // //         Console.Write("Enter a number for factorial: ");
// // //         int num = Convert.ToInt32(Console.ReadLine());
// // //         Console.WriteLine($"Factorial of {num} is {Factorial(num)}");
// // //     }

// // //     static long Factorial(int n)
// // //     {
// // //         return n == 0 ? 1 : n * Factorial(n - 1);
// // //     }
// // // }



// // using System;

// // class Student
// // {
// //     public string Name { get; set; }
// //     public int ID { get; set; }
// //     public double Marks { get; set; }

// //     public Student(string name, int id, double marks)
// //     {
// //         Name = name;
// //         ID = id;
// //         Marks = marks;
// //     }

// //     public string GetGrade()
// //     {
// //         if (Marks >= 90) return "A";
// //         if (Marks >= 75) return "B";
// //         if (Marks >= 60) return "C";
// //         return "F";
// //     }

// //     public void DisplayInfo()
// //     {
// //         Console.WriteLine($"Name: {Name}, ID: {ID}, Marks: {Marks}, Grade: {GetGrade()}");
// //     }
// // }

// // class StudentIITGN : Student
// // {
// //     public string HostelName { get; set; }

// //     public StudentIITGN(string name, int id, double marks, string hostel) 
// //         : base(name, id, marks)
// //     {
// //         HostelName = hostel;
// //     }

// //     public void DisplayIITGNInfo()
// //     {
// //         DisplayInfo();
// //         Console.WriteLine($"Hostel: {HostelName}");
// //     }
// // }

// // class Program
// // {
// //     static void Main()
// //     {
// //         StudentIITGN student = new StudentIITGN("John Doe", 101, 88, "Hostel A");
// //         student.DisplayIITGNInfo();
// //     }
// // }



// using System;

// class ExceptionHandlingDemo
// {
//     static void Main()
//     {
//         try
//         {
//             Console.Write("Enter first number: ");
//             double num1 = Convert.ToDouble(Console.ReadLine());

//             Console.Write("Enter second number: ");
//             double num2 = Convert.ToDouble(Console.ReadLine());

//             if (num2 == 0)
//                 throw new DivideByZeroException("Cannot divide by zero!");

//             Console.WriteLine($"Result: {num1 / num2}");
//         }
//         catch (FormatException)
//         {
//             Console.WriteLine("Invalid input! Please enter a numeric value.");
//         }
//         catch (DivideByZeroException ex)
//         {
//             Console.WriteLine(ex.Message);
//         }
//         finally
//         {
//             Console.WriteLine("End of calculation.");
//         }
//     }
// }



using System;

class ExceptionHandlingDemo
{
    static void Main()
    {
        try
        {
            Console.Write("Enter first number: ");
            double num1 = 12.0;

            Console.Write("Enter second number: ");
            double num2 = 3.0;

            if (num2 == 0)
                throw new DivideByZeroException("Cannot divide by zero!");

            Console.WriteLine($"Result: {num1 / num2}");
        }
        catch (FormatException)
        {
            Console.WriteLine("Invalid input! Please enter a numeric value.");
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine(ex.Message);
        }
        finally
        {
            Console.WriteLine("End of calculation.");
        }
    }
}
