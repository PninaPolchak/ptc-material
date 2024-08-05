package com.mycompany.app;

import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.is;
import org.junit.jupiter.api.Test;
import static org.hamcrest.MatcherAssert.assertThat;


public class AddTest {

   @Test
   public void add() {
      Add add= new Add();
      assertThat(add.calc(10.0, 5.0), is(15.0));
   }

   @Test
   public void addNegative() {
      Add add= new Add();
      assertThat(add.calc(-10.0, 5.0), is(-5.0));
   }

   @Test
   public void addTowNegative() {
      Add add= new Add();
      assertThat(add.calc(-10.0, -5.0), is(-15.0));
   }
}
