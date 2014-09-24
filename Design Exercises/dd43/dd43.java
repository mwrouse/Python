
/**
 * Write a description of class dd43 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class dd43
{
   
}

/**
 * Rectangle Class
 */
class Rectangle
{
    private int length;
    private int width;
    
    /** 
     * Rectangle Constructor
     */
    public Rectangle(int rectLength, int rectWidth)
    {
        length = rectLength;
        width = rectWidth;
    }
    public Rectangle()
    {
        length = 1;
        width = 1;
    }
    
    /**
     * Return rectangle length
     */
    public int GetLength()
    {
        return length;
    }
    
    /** 
     * Return rectangle width
     */
    public int GetWidth()
    {
        return width;
    }
    
    /**
     * Return area of rectangle
     */
    public int GetArea()
    {
        return length * width;
    }
}

