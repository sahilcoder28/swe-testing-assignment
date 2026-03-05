import pytest
from calculator.calc import Calculator
from gui.gui import CalculatorGUI
import tkinter as tk

def test_gui_addition_simulation():
    # Initialize GUI without starting mainloop
    root = tk.Tk()
    gui = CalculatorGUI(root)
    
    # Simulate clicking 5 + 3 =
    for char in "5+3=":
        gui.click(char)
    
    assert gui.display.get() == "8"
    root.destroy()

def test_gui_clear_function():
    root = tk.Tk()
    gui = CalculatorGUI(root)
    
    # Simulate calculation then clear
    for char in "9*2=":
        gui.click(char)
    
    gui.click("C")
    assert gui.display.get() == ""
    root.destroy()