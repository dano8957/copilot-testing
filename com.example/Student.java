package com.example;

/**
 * The Student class represents a student with a name and an ID.
 * It provides methods to get and set the student's name and ID.
 */
public class Student {

    // The name of the student
    private String name;

    // The ID of the student
    private int id;

    /**
     * Constructs a new Student with the specified name and ID.
     *
     * @param name the name of the student
     * @param id the ID of the student
     */
    public Student(String name, int id) {
        this.name = name;
        this.id = id;
    }

    /**
     * Returns the name of the student.
     *
     * @return the name of the student
     */
    public String getName() {
        return name;
    }

    /**
     * Sets the name of the student.
     *
     * @param name the new name of the student
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Returns the ID of the student.
     *
     * @return the ID of the student
     */
    public int getId() {
        return id;
    }

    /**
     * Sets the ID of the student.
     *
     * @param id the new ID of the student
     */
    public void setId(int id) {
        this.id = id;
    }

    /**
     * Returns a string representation of the student.
     * The string representation consists of the student's name and ID.
     *
     * @return a string representation of the student
     */
    @Override
    public String toString() {
        return "Student{name='" + name + "', id=" + id + "}";
    }
}