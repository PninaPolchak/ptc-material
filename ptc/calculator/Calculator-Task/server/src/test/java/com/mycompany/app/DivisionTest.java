package com.mycompany.app;

import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.is;
import org.junit.jupiter.api.Test;
import static org.hamcrest.MatcherAssert.assertThat;

public class DivisionTest {

   @Test
   public void divide() {
      Division division = new Division();
      assertThat(division.calc(5.0, 10.0), is(2.0));
   }

   @Test
   public void divideByZero() {
      Division division = new Division();
      ArithmeticException exception = assertThrows(ArithmeticException.class, () -> division.calc(0.0, 10.0));
      assertEquals(division.getErrStr(), exception.getMessage());
   }
}