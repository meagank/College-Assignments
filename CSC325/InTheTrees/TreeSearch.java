// From <https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/> with modifications to work with strings
// and use mode class accessors and modifiers.
class BinarySearchTree 
{
	Node root;

	BinarySearchTree() {	// initial tree construction
		root = null;
	}

	void deleteKey(String key) {	// initial recursive delete function call
		root = deleteRec(root, key);
	}

	Node deleteRec(Node root, String key) {	// recursive function to delete chosen book
		Node temp;
		// if tree is empty
		if (root == null)
			return root;


		// COMPARETO USED FOR ALL COMPARISONS BETWEEN SEARCHED FOR BOOK AND BOOKS IN TREE
		// COMPARES FIRST CHARACTER IN A STRING AND IF THEY ARE EQUAL IT MOVES TO THE NEXT ONE
		// TILL IT FINDS A MISMATCH IN THEIR CHARACTERS.

		// go down tree to look for given value
		if (key.compareTo(root.getKey()) < 0) // compare the user book to book at current node
			root.setLeft(deleteRec(root.getLeft(), key));
		else if (key.compareTo(root.getKey()) > 0) // compare the user book to book at current node
			root.setRight(deleteRec(root.getRight(), key));
		else {

			// node with one or no child
			if (root.getLeft() == null)
				return root.getRight();
			else if (root.getRight() == null)
				return root.getLeft();

			// node with two children
			temp = minValue(root.getRight());

			// delete successor
			root.setRight(deleteRec(root.getRight(), temp.getKey()));
		}
		return root;
	}

	Node minValue(Node root) {
		Node minv = root;
		while (root.getLeft() != null) {
			minv = root.getLeft();
			root = root.getLeft();
		}
		return minv;
	}

	void insert(String key) {	// initial recursive insert call
		root = insertRec(root, key);
	}

	Node insertRec(Node root, String key) {		// recursive function to add given book
		if (root == null) {			// empty
			root = new Node(key);
			return root;

		}
		// not empty
		if (key.compareTo(root.getKey()) < 0)
			root.setLeft(insertRec(root.getLeft(), key));
		else if (key.compareTo(root.getKey()) > 0)
			root.setRight(insertRec(root.getRight(), key));
		return root;
	}

	void search(String key) {		// initial recursive search call
		Node temp = root;
		temp = searchRec(temp, key);
		if (key.compareTo(temp.getKey()) == 0)
			System.out.println(temp.getKey() + " is in the tree.");
		else
			System.out.println(key + " is not in the tree.");
	}

	Node searchRec(Node root, String key) {		// recursive function to look for given book
		// if the tree is empty or the root is the book being looked for
		Node temp = root;
		if (temp == null || key.compareTo(temp.getKey()) == 0)
			return temp;

		if (temp.getRight() == null || temp.getLeft() == null)
			return temp;
		else if (key.compareTo(temp.getKey()) > 0)
			return searchRec(temp.getRight(), key);
		return searchRec(temp.getLeft(), key);
	}
	
	void inorder() {	// initial recursive inorder print function call
		inorderRec(root);
	}

	void inorderRec(Node root) {   // recursive function to print all books in order
		if (root != null) {
			inorderRec(root.getLeft());
			System.out.print(root.getKey() + "  ");
			inorderRec(root.getRight());
		}
	}

	void preorder() {	// initial recursive pre order print function call
		preorderRec(root);
	}

	void preorderRec(Node root) {	// recursive function to print all books in pre order
		if (root != null) {
			System.out.print(root.getKey() + "  ");
			preorderRec(root.getLeft());
			preorderRec(root.getRight());
		}
	}

	void postorder() {	// initial recursive post order print function call
		postorderRec(root);
	}

	void postorderRec(Node root) {	// recursive function to print all books in post order
		if (root != null) {
			postorderRec(root.getLeft());
			postorderRec(root.getRight());
			System.out.print(root.getKey() + "  ");
		}
	}
}

// From <https://www.geeksforgeeks.org/avl-tree-set-2-deletion/> with modifications to work wth strings 
// and use mode class accessors and modifiers
class AVLTree extends BinarySearchTree {
	
	AVLTree() {	// initial tree construction
		root = null;
	}

	int height(Node a) 
	{
		if (a == null)
			return 0;
		return a.getHeight();
	}

	int maxValue(int x, int y) 
	{
		return (x > y) ? x : y; // if true return x, else y
	}

	Node rightRotate(Node root) 
	{
		Node x = root.getLeft();
		Node y = x.getRight();

		// Perform rotation
		x.setRight(root);
		root.setLeft(y);

		// Update heights
		root.setHeight(maxValue(height(root.getLeft()), height(root.getRight())) + 1);
		x.setHeight(maxValue(height(x.getLeft()), height(x.getRight())) + 1);

		// Return new root
		return x;
	}

	Node leftRotate(Node root) 
	{
		Node y = root.getRight();
		Node x = y.getLeft();

		// Perform rotation
		y.setLeft(root);
		root.setRight(x);

		// Update heights
		root.setHeight(maxValue(height(root.getLeft()), height(root.getRight())) + 1);
		y.setHeight(maxValue(height(y.getLeft()), height(y.getRight())) + 1);

		// Return new root
		return y;
	}

	// Get Balance factor of node N
	int getBalance(Node a) 
	{
		if (a == null)
			return 0;

		return height(a.getLeft()) - height(a.getRight());
	}

	Node add(String key) 
	{
		insert(key);

		// increase height 
		root.setHeight(1 + maxValue(height(root.getRight()), height(root.getLeft())));

		int balance = getBalance(root);

		//********** ROTATIONS **********//
		if (balance > 1 && key.compareTo(root.getLeft().getKey()) < 0) // single rotation
			return rightRotate(root);

		if (balance < -1 && key.compareTo(root.getRight().getKey()) > 0) // " "
			return leftRotate(root);

		if (balance > 1 && key.compareTo(root.getLeft().getKey()) > 0) // double rotation
		{
			root.setLeft(leftRotate(root.getLeft()));
			return rightRotate(root);
		}

		if (balance < -1 && key.compareTo(root.getRight().getKey()) < 0) // " "
		{
			root.setRight(rightRotate(root.getRight()));
			return leftRotate(root);
		}
		return root;
	}

	Node deletion(String key)
	{
		deleteKey(key);

		root.setHeight(1 + maxValue(height(root.getLeft()), height(root.getRight())));
		
		int balance = getBalance(root);

		//********** ROTATIONS **********//*
		if (balance > 1 && getBalance(root.getLeft()) >= 0) 
			return rightRotate(root); 

		if (balance > 1 && getBalance(root.getLeft()) < 0) 
		{ 
			root.setLeft(leftRotate(root.getLeft())); 
			return rightRotate(root); 
		} 

		if (balance < -1 && getBalance(root.getRight()) <= 0) 
			return leftRotate(root); 
 
		if (balance < -1 && getBalance(root.getRight()) > 0) 
		{ 
			root.setRight(rightRotate(root.getRight())); 
			return leftRotate(root); 
		} 
		return root;
	}
}

class RBTree extends BinarySearchTree
{
	private static boolean RED = true;
	private static boolean BLACK = false;
	boolean color;

	RBTree() {	// initial tree construction
		root = null;
	}

	boolean isRed(Node a){
		System.out.println(a.getColor());
		if(a == null)
			return false;
		//a.setColor(RED);
		
		return true;
	}

	void colorFlip(Node a)
   	{  
      	a.setColor(!a.getColor());
     	a.getLeft().setColor(!a.getLeft().getColor());
      	a.getRight().setColor(!a.getRight().getColor());
   	}

	Node leftRotate(Node root) 
	{
		Node y = root.getRight();
		Node x = y.getLeft();

		// Perform rotation
		y.setLeft(root);
		root.setRight(x);

		// Return new root
		return y;
	}

	Node rightRotate(Node root) 
	{
		Node x = root.getLeft();
		Node y = x.getRight();

		x.setColor(x.getRight().getColor());
		x.getRight().setColor(RED);

		// Perform rotation
		x.setRight(root);
		root.setLeft(y);

		// Return new root
		return x;
	}
	void put(String key){
		root = insertion(root, key);
	}
	Node insertion(Node root, String key) {		// recursive function to add given book
		insert(key);

		/*
		if(isRed(root.getRight()))
			return leftRotate(root);
		
		if(isRed(root.getLeft()) && isRed(root.getLeft().getLeft()))
			return rightRotate(root);

		if(isRed(root.getLeft()) && isRed(root.getRight()))
			colorFlip(root);

		*/

		return root;
	}

	Node deleting(String key){
		deleteKey(key);

		return root;
	}
}
