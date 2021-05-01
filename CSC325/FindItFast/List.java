
/* ***************************************************
 * Meagan Kropp
 * 10/15/2020
 * List.java
 *
 * Creates a linked list (created in class with teacher during CSC 220).
 *************************************************** */

// the Node class
class Node
{
	private char data;
	private Node link;

	// constructor
	public Node()
	{
		this.data = ' ';
		this.link = null;
	}

	// accessor and mutator for the data component
	public char getData()
	{
		return this.data;
	}

	public void setData(char data)
	{
		this.data = data;
	}

	// accessor and mutator for the link component
	public Node getLink()
	{
		return this.link;
	}

	public void setLink(Node link)
	{
		this.link = link;
	}
}

// the List class
public class List
{
	public static final int MAX_SIZE = 36000;

	private Node head;
	private Node tail;
	private Node curr;
	private int num_items;

	// constructor
	// remember that an empty list has a "size" of 0 and its "position" is at -1
	public List()
	{
		head = tail = curr = null;
		num_items = 0;
	}

	// copy constructor
	// clones the list l and sets the last element as the current
	public List(List l)
	{
		head = tail = curr = null;
		num_items = 0;
		Node temp = l.head;

		while(temp != null)
		{
			this.InsertAfter(temp.getData());
			temp = temp.getLink();
		}
	}

	// navigates to the beginning of the list
	public void First()
	{
		curr = head;
	}

	// navigates to the end of the list
	// the end of the list is at the last valid item in the list
	public void Last()
	{
		curr = tail;
	}

	// navigates to the specified element (0-index)
	// this should not be possible for an empty list
	// this should not be possible for invalid positions
	public void SetPos(int pos)
	{
		if(!IsEmpty() && pos < num_items && pos >= 0)
		{
			curr = head;
			for(int i = 0; i < pos; i ++)
				curr = curr.getLink();
		}	
	}

	// navigates to the previous element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Prev()
	{
		if(!IsEmpty())
		{
			Node temp = head;
			while (temp.getLink() != curr)
			{
				temp = temp.getLink();
			}
			curr = temp;
		}
	}

	// navigates to the next element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Next()
	{
		if(!IsEmpty() && curr != tail)
			curr = curr.getLink();
	}

	// returns the location of the current element (or -1)
	public int GetPos()
	{
		if(IsEmpty())
		{
			return -1;
		}
		
		Node temp = head;
		int i = 0;
		while (temp != curr && temp != null)
		{
			i++;
			temp = temp.getLink();
		}
		return i;
	}

	// returns the value of the current element (or -1)
	public char GetValue()
	{
		if(IsEmpty())
			return ' ';
		return curr.getData();
	}

	// returns the size of the list
	// size does not imply capacity
	public int GetSize()
	{
		return (num_items);
	}

	// inserts an item before the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertBefore(char data)
	{
		if(!IsFull())
		{
			if(IsEmpty())
				InsertAfter(data);
			else if(head == curr)
			{
				Node n = new Node();
				n.setData(data);
				n.setLink(head);
				curr = head = n;
				num_items++;
			}
			else
			{
				Prev();
				InsertAfter(data);
			}
		}			
	}

	// inserts an item after the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertAfter(char data)
	{
		if(!IsFull())
		{
			Node n = new Node();
			n.setData(data);

			if (IsEmpty())
			{
				head = curr = tail = n;
			}
			else if(curr == tail)
			{
				tail.setLink(n);
				tail = curr = n;
			}
			else
			{
				n.setLink(curr.getLink());
				curr.setLink(n);
				curr = n;
			}
			num_items++; 
		}
	}

	// removes the current element (collapsing the list)
	// this should not be possible for an empty list. If possible,
	// following element becomes new current element.
	public void Remove()
	{
		if(!IsEmpty())
		{
			if(head == curr)
			{
				if (head == tail)
					tail = null;
				head = curr = curr.getLink();
			}
			else if (curr == tail)
			{
				Prev();
				tail = curr;
				tail.setLink(null);
			}
			else
			{
				Prev();
				curr.setLink(curr.getLink().getLink());
				Next();
			}
			num_items--;
		}
	}

	// replaces the value of the current element with the specified value
	// this should not be possible for an empty list
	public void Replace(char data)
	{
		if(!IsEmpty())
			curr.setData(data);
	}

	// returns if the list is empty
	public boolean IsEmpty()
	{
		return (num_items == 0);
	}

	// returns if the list is full
	public boolean IsFull()
	{
		return (num_items == MAX_SIZE);		
	}

	// returns if two lists are equal (by value)
	public boolean Equals(List l)
	{
		if(this.GetSize() != l.GetSize())
			return false;
		
		Node a = head, b = l.head;
		while(a != null && b != null)
		{
			if(a.getData() != b.getData())
				return false;
			a = a.getLink();
			b = b.getLink();
		}
		return true;
	}

	// returns the concatenation of two lists
	// l should not be modified
	// l should be concatenated to the end of *this
	// the returned list should not exceed MAX_SIZE elements
	// the last element of the new list is the current
	public List Add(List l)
	{
		List sum = new List(this);
		Node temp = l.head;
		while (temp != null)
		{
			sum.InsertAfter(temp.getData());
			temp = temp.getLink();
		}
		return sum;
	}

	// returns a string representation of the entire list (e.g., 1 2 3 4 5)
	// the string "NULL" should be returned for an empty list
	public String toString()
	{
		if(IsEmpty())
		{
			return "NULL";
		}
		String result = "";
		Node temp = head;
		while (temp != null)
		{
			result += (temp.getData() + " ");
			temp = temp.getLink();
		}
		return result;
	}
}
