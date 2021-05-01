/* *********************************************
* Name: Meagan Kropp
* Date: April 18, 2021
* Description: Take in a file filled with book names and insert them into a tree, search for a user specified book, 
* and delete a user specified book.  Includes time analysis for each thing done.
* Uses TreeSearch.java to create the trees and has the needed constructors.
********************************************** */

import java.io.*; 
import java.nio.file.*;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;
import java.util.Arrays;


class Trees
{
	public static void main(String[] args) throws Exception
    {
		int choice;
		String books = " ";
		String bookSearch;
		String bookDelete;

		Scanner ln = new Scanner(System.in);	
		
		System.out.print("Enter the book you want to look for: ");
		bookSearch = ln.nextLine();

		System.out.print("Would you like to look for it in input 1 or 2? ");
		choice = ln.nextInt();
		

		if(choice == 1)
	    	books = new String(Files.readAllBytes(Paths.get("SciFiLiBooks.txt")));
		else if(choice == 2)
			books = new String(Files.readAllBytes(Paths.get("SciFiLiSorted.txt")));
		else
			System.out.println("Not a possible choice.");

		
		String[] arrayString = books.split("\\r?\\n");

		ln.nextLine();
		System.out.print("Enter the book you want to delete: ");
		bookDelete = ln.nextLine();

		ln.close();

		/*PrintStream console = System.out;
		File file = new File("out.txt");
		FileOutputStream output = new FileOutputStream(file);
		PrintStream print = new PrintStream(output);
		System.setOut(print);*/
	
		long totalBST = BST(arrayString, bookSearch, bookDelete);
		long totalAVL = AVL(arrayString, bookSearch, bookDelete);
		long totalRB = RB(arrayString, bookSearch, bookDelete);
		System.out.println("Total time to do all BST functions is " + ((double)totalBST)/1000000 + " milliseconds. ");
		System.out.println("Total time to do all AVL functions is " + ((double)totalAVL)/1000000 + " milliseconds. ");
		System.out.println("Total time to do all RB functions is " + ((double)totalRB)/1000000 + " milliseconds. \n ");

		if (totalBST < totalAVL && totalBST < totalRB)
			System.out.println("The binary search tree was the fastest.");
		else if (totalAVL < totalBST && totalAVL < totalRB)
			System.out.println("The AVL tree was the fastest.");
		else
			System.out.println("The RB tree was the fastest.");


		/*System.setOut(console);
		System.out.println("Output sent to out.txt");*/
	}
//****************************************************************************************************************************************
	public static long BST(String [] array, String find, String delete)
	{
		
		long totalTime = 0;
		long sT = System.nanoTime();
		BinarySearchTree tree = new BinarySearchTree();
		
		for(int i = 0; i < array.length; i++)
		{
			tree.insert(array[i]);
		}

		long eT = System.nanoTime();
		long total = eT - sT;
		totalTime = totalTime + total;
		System.out.println("\nBST took " + ((double)total)/1000000 + " milliseconds to make the tree.");
		
		
		sT = System.nanoTime();
		tree.search(find);
		eT = System.nanoTime();
		total = eT - sT;
		totalTime += total;
		System.out.println("BST took " + ((double)total)/1000000 + " milliseconds to search for " + find + ".");

		
			
		sT = System.nanoTime();
		tree.deleteKey(delete);
		eT = System.nanoTime();
		total = eT - sT;
		totalTime += total;
		System.out.println("BST took " + ((double)total)/1000000 + " milliseconds to delete " + delete + " from the tree. \n");
		return totalTime;
		
	}
//****************************************************************************************************************************************
	public static long AVL(String [] array, String find, String delete)
	{
		long totalTime = 0;
		long sT = System.nanoTime();
		AVLTree tree = new AVLTree();

		for(int i = 0; i < array.length; i++)
		{
			tree.add(array[i]);
		}

		long eT = System.nanoTime();
		long total = eT - sT;
		totalTime = totalTime + total;
		System.out.println("AVL took " + ((double)total)/1000000 + " milliseconds to make the tree.");
		
		sT = System.nanoTime();
		tree.search(find);				// uses bst search as they are done the same way
		eT = System.nanoTime();
		total = eT - sT;
		totalTime = totalTime + total;
		System.out.println("AVL took " + ((double)total)/1000000 + " milliseconds to search for " + find + ".");

		sT = System.nanoTime();
		tree.deletion(delete);
		eT = System.nanoTime();
		total = eT - sT;
		totalTime = totalTime + total;
		System.out.println("AVL took " + ((double)total)/1000000 + " milliseconds to delete " + delete + " from the tree. \n");

		return totalTime;
	}
//****************************************************************************************************************************************
	public static long RB(String [] array, String find, String delete){
		long totalTime = 0;
		long sT = System.nanoTime();
		RBTree tree = new RBTree();

		for(int i = 0; i < array.length; i++)
		{
			tree.put(array[i]);
		}

		long eT = System.nanoTime();
		long total = eT - sT;
		totalTime = totalTime + total;
		System.out.println("RB took " + ((double)total)/1000000 + " milliseconds to make the tree.");
		
		/*sT = System.nanoTime();
		tree.search(find);				// uses bst search as they are done the same way
		eT = System.nanoTime();
		total = eT - sT;
		totalTime = totalTime + total;
		System.out.println("RB took " + ((double)total)/1000000 + " milliseconds to search for " + find + "."); */

		sT = System.nanoTime();
		tree.deleting(delete);
		eT = System.nanoTime();
		total = eT - sT;
		totalTime = totalTime + total;
		System.out.println("RB took " + ((double)total)/1000000 + " milliseconds to delete " + delete + " from the tree. \n");

		return totalTime;
	}
}