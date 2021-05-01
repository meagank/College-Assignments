//*******************************************************************************************************************************
//Name: Meagan Kropp
//Date: September 28, 2020
//Description: Take in a 2D array of numbers and find the largest sum of 4 digits in the same row.
//*******************************************************************************************************************************


import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

class LargestSum
{
	public static void main(String [] args) throws Exception
	{
		// CONSTANTS FOR ROW AND COL SIZE
		int row = 20;
		int col = 20;

		ArrayList<Integer> x = readFile();
		int[][] nums2 = new int[row][col];
	
		//convert arraylist to 1D array
		Integer[] tempArray = x.toArray(new Integer[0]);

		//convert 1D array to a 20x20 2D array
		//didn't know if it was possible to convert an arraylist to 2D array
		//so it was done in 2 steps
		for(int i = 0; i < row; i++)
		{
			for(int j = 0; j < col; j++)
			{
				nums2[i][j] = tempArray[j + (i*10)];
			}
		}
		System.out.println("");
		System.out.println("Max horizontal sum: " + largestHor(nums2));
	}

	public static int largestHor (int[][] arr)
	{
		int temp = 0;
		int gSum = 0;

		// used 19 & 16 b/c array index starts at 0
		for(int k = 0; k < 19; k++)
		{
			for(int i = 0; i < 16; i++)
			{
				for(int j = i; j < i + 4; j++)
				{
					temp = temp + arr[k][j];
					
				}
				if(temp > gSum)
				{
					gSum = temp;
				}
				temp = 0;
			}
		}
		return gSum;
	}


	public static ArrayList<Integer> readFile()
	{
		ArrayList<Integer> nums = new ArrayList<Integer>();

		
		Scanner sc = new Scanner(System.in);
		while(sc.hasNextInt())
			nums.add(sc.nextInt());
		
		//System.out.println(nums);
		return nums;
	}
}