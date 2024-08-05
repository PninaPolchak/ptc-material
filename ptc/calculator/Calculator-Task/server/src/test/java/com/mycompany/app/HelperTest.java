package com.mycompany.app;

import static com.mycompany.app.Helper.*;
import org.junit.Test;
import static org.junit.Assert.*;


public class HelperTest {

    @Test
    public void SecondOperatorIsCloseBracket() {
        assertEquals(false, isFirst('*', ')'));
    }

    @Test
    public void SecondOperatorIsOpenBracket() {
        assertEquals(false, isFirst('+', '('));
    }

    @Test
    public void FirstOperatorIsMultiplication() {
        assertEquals(false, isFirst('*', '+'));
    }

    @Test
    public void FirstOperatorIsDivision() {
        assertEquals(false, isFirst('/', '-'));
    }

    @Test
    public void FirstOperatorIsAdd() {
        assertEquals(true, isFirst('+', '/'));
    }

    @Test
    public void FirstOperatorIsSubtraction() {
        assertEquals(true, isFirst('-', '*'));
    }

    @Test
    public void samePriorityAddAndSubtraction() {
        assertEquals(true, isFirst('-', '+'));
    }

    @Test
    public void samePriorityDivisionAndMultiplication() {
        assertEquals(true, isFirst('*', '/'));
    }

    @Test
    public void testIsDigit() {
        assertEquals(true, isDigit('1'));
    }

    @Test
    public void testIsNotDigit() {
        assertEquals(false, isDigit('h'));
    }

    @Test
    public void testIsDot() {
        assertEquals(true, isDigitOrDot('.'));
    }

    @Test
    public void testIsNotDot() {
        assertEquals(false, isDigitOrDot('*'));
    }
}