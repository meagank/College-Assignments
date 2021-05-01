/* *********************************************
* Name: Meagan Kropp
* Date: March 21, 2021
* Description: Take in a pattern and search for it in 1 of 2 text files.
* Notes: Professor given text files are hard-coded in, must select which one to use.
* Uses List.java to create the Linked List and all its constructors.
********************************************** */
import java.io.*; 
import java.nio.file.*;;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;
import java.util.Arrays;



public class FindItFast 
{
	public static void main(String[] args) throws Exception 
	{ 
		int choice;
		String pattern;
		String data = " ";
		
		Scanner ln = new Scanner(System.in);	
		System.out.print("Enter pattern you are looking for: ");
		pattern = ln.next();
		
		System.out.print("Enter 1 for input1, 2 for input2: ");
		choice = ln.nextInt();
	

	/*	BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		while(in.readLine() != null) {
			sb.append(in.readLine()).append("\n");
		}
		String data = sb.toString();
		in.close();

	*/
		// hardcoded in the two given input files given
		if(choice == 1)
	    		data = new String(Files.readAllBytes(Paths.get("prog1input1.txt")));
		else if(choice == 2)
			data = new String(Files.readAllBytes(Paths.get("prog1input2.txt")));
		else
			System.out.println("Not a possible choice.");
		
		List text = new List();
		for (int i = 0; i < data.length(); i++){
			text.InsertAfter(data.charAt(i));	
		}
		
	
		List patt = new List();
		for (int j = 0; j < pattern.length(); j++){
			patt.InsertAfter(pattern.charAt(j));
		}

		PrintStream console = System.out;
		File file = new File("out.txt");
		FileOutputStream output = new FileOutputStream(file);
		PrintStream print = new PrintStream(output);
		System.setOut(print);

		long sT = System.nanoTime();
		int[] found = bruteForce(text, patt);
		long eT = System.nanoTime();
		long totalBF = eT - sT;
		System.out.println("Brute Force Search took " + ((double)totalBF)/1000000 + " milliseconds.");
		
	
		sT = System.nanoTime();
		int[] foundTwo = KMP(text, patt);
		eT = System.nanoTime();
		long totalKMP = eT - sT;
		System.out.println("KMP Search took " + ((double)totalKMP)/1000000 + " milliseconds.");

		sT = System.nanoTime();
	
		// currently only uses good suffix and only gives first instance of the pattern
		BM(text, patt); 
		eT = System.nanoTime();
		long totalBM = eT - sT;
		System.out.println("Boyer-Moore Search took " + ((double)totalBM)/1000000 + " milliseconds.");


		if (totalBF < totalKMP && totalBF < totalBM)
			System.out.println("Brute Force is fastest.");
		else if (totalKMP < totalBF && totalKMP < totalBM)
			System.out.println("KMP is fastest.");
		else
			System.out.println("Boyer-Moore is fastest.");

		System.out.print("Brute force finds it at: ");
		for(int i = 0; i < found.length; i++){
			if(found[i] == 0) continue; // only prints filled indexes
				System.out.print((found[i] - 1) + " ");  // subtracted by 1 because of way array is stored in Brute Force function
		}
		System.out.print("\n");

		System.out.print("KMP finds it at: ");
		for(int i = 0; i < foundTwo.length; i++){
			if(foundTwo[i] == 0) continue; // only prints filled indexes
				System.out.print((foundTwo[i] - 5) + " ");  // subtracted by 5 because it gives index of last node, and starts at 1 instead of 0.
		}
		System.out.print("\n");

		System.setOut(console);
		System.out.println("Output sent to out.txt");
		
		
		
	} 
//****************************************************************************************************************************************
	// returns the time it took to search the whole linked list for every instance of the pattern
	public static int[] bruteForce(List t, List p)
	{
		int[] index = new int[100000];
		int k = 0;
		// sets each ll to its first node
		t.First();
		p.First();

		for (int i = 0; i < t.GetSize() - p.GetSize(); i++){
			int j;
			for (j = 0; j < p.GetSize(); j++){
				// if they have the same character, get their next character
				if(t.GetValue() == p.GetValue()){
					t.Next();
					p.Next();
				}
				// if node values are different, break out of the inner loop
				else{
					break;
				}
			}
			if(j == p.GetSize()){
				index[k] = i;
				k++;	
			}
			// sets p back to its first node
			p.First();
			t.SetPos(i);
		}
		return index;

	}
//****************************************************************************************************************************************
	// <https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/> used as reference for Linked List KMP
	// site uses Strings, converted to use Linked Lists and its corresponding functions

	// returns the time it took to search the whole linked list for every instance of the pattern
	public static int[] KMP(List t, List p)
	{
		int[] index = new int[100000];
		int k = 0;
		int[] table = createTable(p);
		
		int j = 0;
		int i = 0;
		while( i < t.GetSize()){
			t.SetPos(i);
			p.SetPos(j);
			if(t.GetValue() == p.GetValue()){
				i++;
				j++;
			}
			if(j == p.GetSize()){
				j = table[j-1];
			
				index[k] = i;
				k++;
			}
			else if (i < t.GetSize() && t.GetValue() != p.GetValue()){
				if(j != 0)
					j = table[j-1];
				else
					i = i+1;
			}
		}
		return index;	
	}

	// returns the failure function table
	// also based off of code from <https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/>
	public static int[] createTable(List p){
		int[] table = new int[p.GetSize()];
		table[0] = 0;
		int i = 1;
		int len = 0;
		
		// creates a copy of the pattern list as to compare two of its nodes values.
		List b = new List(p);
		
		while( i < p.GetSize()){
			p.SetPos(i);
			b.SetPos(len);
			if(p.GetValue() == b.GetValue()){
				len++;
				table[i] = len;
				i++;
			}
			else{
				if(len != 0)
					len = table[len - 1];
				else{
					table[i] = len;
					i++;
				}
			}
		}
		return table;
	}
//****************************************************************************************************************************************
	

	// Based on <https://www.geeksforgeeks.org/boyer-moore-algorithm-good-suffix-heuristic/>
	public static void BM(List t, List p){
		
		int[] border = new int[p.GetSize() + 1];
		int[] shiftA = new int[p.GetSize() + 1];

		for(int i = 0; i < p.GetSize(); i++){
			shiftA[i] = 0;
		}

		fullSuffix(shiftA, border, p);
		partialSuffix(shiftA, border, p);

		int shift = 0;
		while(shift <= (t.GetSize() - p.GetSize())){
			int j = p.GetSize() - 1;
			p.SetPos(j);
			t.SetPos(shift + j);
			while(j >= 0 && p.GetValue() == t.GetValue())
				j--;
			if(j < 0)
				shift += shiftA[0];
			else
				shift += shiftA[j+1];
	
			}
	
	}		

	public static void fullSuffix(int[] shift, int[] border,List p){
		int m = p.GetSize();
		int i = m;
		int j = m + 1;
		border[i] = j;

		List b = new List(p);
		
		while(i > 0) {
			p.SetPos(i - 1);
			b.SetPos(j - 1);
      			while(j <= m && p.GetValue() != b.GetValue() ) {
        			 if(shift[j] == 0)
            				shift[j] = j-i;     
         			j = border[j];   
			}
			i--;
			j--;
			border[i] = j;
		}		
	}
		
	public static void partialSuffix(int[] shift, int[] border,List p){
		int m = p.GetSize();
		int j;
		j = border[0];
	
		 for(int i = 0; i < m; i++) {
     			 if(shift[i] == 0){
				shift[i] = j;        //when shift is 0, set shift to border value
         			if(i == j)
            				j = border[j]; 
			}
		}
	}
} 