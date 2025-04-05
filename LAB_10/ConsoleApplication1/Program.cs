using System;

class DebuggingDemo
{
    static void Main()
    {
        Console.WriteLine("🔍 Debugging in VS Code - Start!");

        // 1️⃣ Set a breakpoint here to inspect 'num'
        Console.Write("Enter a number: ");
        int num = Convert.ToInt32(Console.ReadLine());

        // 2️⃣ Set a breakpoint here to inspect 'result'
        int result = Factorial(num);
        Console.WriteLine($"Factorial of {num} is {result}");

        // 3️⃣ Check how the loop works
        PrintNumbers(num);

        Console.WriteLine("✅ Debugging Complete!");
    }

    // Recursive Function (Step Into with F11)
    static int Factorial(int n)
    {
        if (n == 0) return 1;
        return n * Factorial(n - 1); // Debugging: Step Into (F11) here!
    }

    // Loop Example (Step Over with F10)
    static void PrintNumbers(int count)
    {
        for (int i = 1; i <= count; i++)
        {
            Console.WriteLine($"Number: {i}"); // Observe values changing
        }
    }
}
