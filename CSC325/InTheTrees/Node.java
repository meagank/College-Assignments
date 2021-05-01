class Node 
{
    String key;	// for all trees
    Node left;	// "           "
	Node right;	// "           "
	int height;	// for avl tree
	boolean color;
 
        public Node(String item)
        {
        	this.key = item;	// for all trees
        	this.left = null;	// "           "
			this.right = null;	// "           "
			this.height = height;	// for avl tree
			this.color = color;
        }

		public Node()
    	{
			this.key = " ";
			this.left = null;
			this.right = null;
			this.height = 1;
			this.color = color;  // new nodes start with color red, red = 1 black = 0
    	}

    	// all the accessors and mutators
		public void setHeight(int height)
    	{
			this.height = height;
    	}
	
    	public void setKey(String key)
    	{
			this.key = key;
    	}

    	public void setLeft(Node left)
    	{
			this.left = left;
    	}

    	public void setRight(Node right)
    	{
			this.right = right;
    	}
		public void setColor(boolean color)
    	{
			this.color = color;
    	}

		public int getHeight()
    	{
			return this.height;
    	}

    	public String getKey()
    	{
			return this.key;
    	}

    	public Node getLeft()
    	{
			return this.left;
    	}

    	public Node getRight()
    	{
			return this.right;
    	}

		public boolean getColor()
    	{
			return this.color;
    	}
}
 
