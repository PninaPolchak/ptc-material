import { useState } from "react";
import axios from "axios";

import Wrapper from "./components/Wrapper";
import Screen from "./components/Screen";
import ButtonBox from "./components/ButtonBox";
import Button from "./components/Button";

const btnValues = [
  ["C", "(", ")", "/"],
  [7, 8, 9, "x"],
  [4, 5, 6, "-"],
  [1, 2, 3, "+"],
  [0, ".", "="]
];

 const App = () => {
  let [calc, setCalc] = useState({
    exercise: "0",
    result: "0"
  })

  const fixSyntaxInExercise = () => {
    let fixedExercise = calc.exercise.replace("+", "%2B");
    let fixedExercise2 = fixedExercise.replace("x", "*");
    return fixedExercise2;
  }

  const connect = async (fixedExercise) => {
    try {
      let response = await axios.get(`http://localhost:8080/api?exercise=${fixedExercise}`);
    setCalc({
      ...calc,
      result: response.data,
      exercise: "0"
    });
    }
    catch (err) {
      let errMsg =`error in connect to server: ${err}`;
      return errMsg;
    }
  };

  function is_numeric(str) {
    return /^\d+$/.test(str);
  }

  const correctExerciseWithBracket = (value) => {
    let ending = calc.exercise.charAt(calc.exercise.length - 1);
    return ((value === "(" && !is_numeric(ending))
      || (value === ")" && is_numeric(ending)))
  }

  const correctExercise = (value) => {
    let ending = calc.exercise.charAt(calc.exercise.length - 1);
    if (ending !== value && calc.exercise !== "0") {
      if (value === "(" || value === ")") {
        return correctExerciseWithBracket(value);
      }
      return (is_numeric(ending) || ending === ")");
    }
  }

  const equalsClickHandler = async () => {
    let newExercise = fixSyntaxInExercise();
    connect(newExercise);
  }

  const numClickHandler = (e) => {
    e.preventDefault();
    let value = e.target.innerHTML;
    setCalc({
      ...calc,
      exercise:
        calc.exercise === "0"
          ? value
          : calc.exercise + value
    });
  };

  const operatorClickHandler = (e) => {
    e.preventDefault();
    let value = e.target.innerHTML;
    if (correctExercise(value)) {
      setCalc({
        ...calc,
        exercise:
          calc.exercise === "0"
            ? value
            : calc.exercise + value
      })
    }
  };

  const resetClickHandler = () => {
    setCalc({
      ...calc,
      exercise: "0",
      result: "0"
    })
  };

  const buttonClickHandler = async (e, btn) => {
    btn === "C"
      ? resetClickHandler()
      : btn === "="
        ? equalsClickHandler()
        : is_numeric(btn)
          ? numClickHandler(e)
          : operatorClickHandler(e)
  }

  return (
    <Wrapper>
      <Screen value={calc.exercise !== "0" ? calc.exercise : calc.result} />
      <ButtonBox>
        {btnValues.flat().map((btn, i) => {
          return (
            <Button
              key={i}
              className={btn === "=" ? "equals" : ""}
              value={btn}
              onClick={(e) => buttonClickHandler(e, btn)}
            />
          );
        })}
      </ButtonBox>
    </Wrapper>
  );
};

export default App;