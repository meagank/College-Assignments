//*******************************************************************************************************************************
//Name: Meagan Kropp
//Date: September 28, 2020
//Description: Take  in integer inputs from a file, find the leading digit, and make a chart to represent occurences in the file.
//*******************************************************************************************************************************


import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.io.*;

class Table
{
	public static void main(String [] args)
	{			
		int[] leadDig = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

		ArrayList<Integer> x = readFile();
		ArrayList<Integer> occurences =  new ArrayList<Integer>(); 
		occurences = getNum(x);

		double arrayLength;
		arrayLength = x.size();
		int total = 0;
		double totalPercent = 0.0;

		double percentage = 0.0;
		
		//************ TABLE ELEMENTS ************			
		String header1 = "Leading Digit";
		String header2 = "Count";
		String header3 = "%";
		String divider = "------------------------------------";
		String divider2 = "====================================";
		String footer1 = "Total";

		//****************** SETTING UP TABLE ****************** 
		System.out.println(divider);
		System.out.printf("%-15s %-10s %5s %n", header1, header2, header3);
		System.out.println(divider);

		//ADD NUMBERS TO TABLE
		for(int ld: leadDig)
		{
			total = total + occurences.get(ld);
			percentage = (occurences.get(ld) / arrayLength) * 100;
			totalPercent = totalPercent + percentage;
			System.out.printf("%-15s %-10s %5.2f %-5s %n", ld, occurences.get(ld), percentage, "%");
		}
		System.out.println(divider);
		System.out.printf("%-15s %-10s %5.2f %-5s %n", footer1, total, totalPercent, "%");
		System.out.println(divider2);
	}
	
	
	public static ArrayList<Integer> getNum (ArrayList<Integer> arr)
	{
		ArrayList<Integer> arrList = new ArrayList<Integer>(Collections.nCopies(10,0));
		int temp = 0;
		for(int i = 0; i < arr.size(); i++)
		{
			int num = arr.get(i);
			while(num >= 10)
				num = num / 10;
			temp = arrList.get(num);
			temp++;
			arrList.set(num, temp);		
		}
		return arrList;
	}
	
	public static ArrayList<Integer> readFile()
	{
		ArrayList<Integer> data = new ArrayList<Integer>();
		
		Scanner sc = new Scanner(System.in);
		while(sc.hasNextInt())
			data.add(sc.nextInt());

		return data;
	}
}


	