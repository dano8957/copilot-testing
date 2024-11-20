package com.example;

import org.junit.Test;
import static org.junit.Assert.*;

public class StudentTest {

    @Test
    public void testStudentAttributes() {
        Student student = new Student("John", "Doe", "1234567890", "123 Main St", "john.doe@example.com");

        assertEquals("John", student.getFirstName());
        assertEquals("Doe", student.getLastName());
        assertEquals("1234567890", student.getPhoneNumber());
        assertEquals("123 Main St", student.getAddress());
        assertEquals("john.doe@example.com", student.getContactEmail());
    }

    @Test
    public void testSetters() {
        Student student = new Student("John", "Doe", "1234567890", "123 Main St", "john.doe@example.com");

        student.setFirstName("Jane");
        student.setLastName("Smith");
        student.setPhoneNumber("0987654321");
        student.setAddress("456 Elm St");
        student.setContactEmail("jane.smith@example.com");

        assertEquals("Jane", student.getFirstName());
        assertEquals("Smith", student.getLastName());
        assertEquals("0987654321", student.getPhoneNumber());
        assertEquals("456 Elm St", student.getAddress());
        assertEquals("jane.smith@example.com", student.getContactEmail());
    }
}