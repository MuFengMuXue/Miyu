# Gamepad Navigation

This page covers different topics related to controling Heroic using a gamepad.

# Gamepad API

Heroic uses the [Gamepad API](https://developer.mozilla.org/en-US/docs/Web/API/Gamepad_API) to detect interactions with the gamepad. Make sure your controller is detected in https://gamepad-tester.com using a chromium-based browser (using the Chromium browser directly is prefered) before reporting a controller not working (Firefox may report different name and layout for the same controller).

# Interactions

These are the currently implemented interactions:

## padUp / padDown / padLeft / padRight

Moves the focus to the next element in the specified direction. Holding the action repeats every 500ms.

## leftStickUp / leftStickDown / leftStickLeft / leftStickRight

Moves the focus to the next element in the specified direction. Holding the action repeats every 250ms.

## rightStickUp / rightStickDown

Scrolls the main content by 50px in the specified direction. Holding the action repeats every 50ms.

## mainAction

It executes the main action associated to the currently focused object:

- Search Input: show and focus the virtual keyboard
- Virtual keyboard buttons: type a letter in the search input
- Game card: if the game is installed, run the game
- anywhere else: acts as a click on the element

## back

It executes a back action in the browser history in most cases to go back to the previous screen. Exceptions are:

- Virtual keyboard is visible: remove keyboard

## altAction

Executes an alternative action depending on specific conditions:

- Virtual keyboard is visible: delete the last character in the input
- Focused element is the game card: open the game screen

# Controlling the Virtual Keyboard

Heroic uses [simple-keyboard](https://virtual-keyboard.js.org) for the virtual keyboard.

## Activate keyboard

Press the `mainAction` button when focusing the search input.

## Writing

Pressing the `mainAction` button when focusing the desired letter will append the letter to the input.

## Deleting

Pressing the `altAction` button will remove the last letter from the input.

## Closing the keyboard

Pressing the `back` button will dismiss the keyboard.

# Layouts

Each gamepad may have its own layout. We need to code the mapping between the generic `BX` and axes reported by the Gamepad API to valid actions for each device.

## Current layouts

### Xbox layout

Matches any controller id with the words `xbox` or `microsoft` in it, or product id `0268`.

```
B0 = A (mapped as mainAction)
B1 = B (mapped as back)
B2 = X
B3 = Y (mapped as altAction)
B4 = LB
B5 = RB
B6 = LT // supports a `.value` method with a value between 0 and 1
B7 = RT // supports a `.value` method with a value between 0 and 1
B8 = view
B9 = menu
B10 = L3 // pressing the left stick
B11 = R3 // pressing the right stick
B12 = Dpad Up (mapped as padUp)
B13 = Dpad Down (mapped as padDown)
B14 = Dpad Left (mapped as padLeft)
B15 = Dpad Right (mapped as padRight)
B16 = XBOX
AXIS 0 = leftAxisX (mapped as leftStickLeft and leftStickRight) // -1 = left, 1 = right
AXIS 1 = leftAxisY (mapped as leftStickUp and leftStickDown) // -1 = up, 1 = down
AXIS 2 = rightAxisX // -1 = left, 1 = right
AXIS 3 = rightAxisY (mapped as rightStickUp and rightStickDown) // -1 = up, 1 = down
```

### Playstation 3

Matches any controller id with the words `PS3`, `PS4`, or `PLAYSTATION` in it, or product id `0268`.

```
B0 = X (mapped as mainAction)
B1 = Circle (mapped as back)
B2 = Square
B3 = Triangle (mapped as altAction)
B4 = LB
B5 = RB
B6 = LT // supports a `.value` method with a value between 0 and 1
B7 = RT // supports a `.value` method with a value between 0 and 1
B8 = Select
B9 = Start
B10 = L3 // pressing the left stick
B11 = R3 // pressing the right stick
B12 = Dpad Up (mapped as padUp)
B13 = Dpad Down (mapped as padDown)
B14 = Dpad Left (mapped as padLeft)
B15 = Dpad Right (mapped as padRight)
B16 = PS Button
AXIS 0 = leftAxisX (mapped as leftStickLeft and leftStickRight) // -1 = left, 1 = right
AXIS 1 = leftAxisY (mapped as leftStickUp and leftStickDown) // -1 = up, 1 = down
AXIS 2 = rightAxisX // -1 = left, 1 = right
AXIS 3 = rightAxisY (mapped as rightStickUp and rightStickDown) // -1 = up, 1 = down
```

### Playstation 5

Matches any controller id with the product id `0ce6` in the controller id.

```
B0 = Circle (mapped as back)
B1 = Triangle (mapped as altAction)
B2 = X (mapped as mainAction)
B3 = Square
B4 = LB
B5 = RB
B6 = rightAxisX // supports a `.value` method with a value between 0 (left) and 1 (right)
B7 = rightAxisY // supports a `.value` method with a value between 0 (up) and 1 (down)
B8 = Select
B9 = Start
B10 = L3 // pressing the left stick
B11 = R3 // pressing the right stick
B12 = Dpad Up (mapped as padUp)
B13 = Dpad Down (mapped as padDown)
B14 = Dpad Left (mapped as padLeft)
B15 = Dpad Right (mapped as padRight)
AXIS 0 = leftAxisX (mapped as leftStickLeft and leftStickRight) // -1 = left, 1 = right
AXIS 1 = leftAxisY (mapped as leftStickUp and leftStickDown) // -1 = up, 1 = down
```

### GameCube

Matches any controller id with the word `gamecube` in it, or product id `0337`.

```
B0 = A (mapped as mainAction)
B1 = X
B2 = Y (mapped as altAction)
B3 = B (mapped as back)
B4 = LT // gets "pressed" as when the trigger is fully pressed
B5 = RT // gets "pressed" as when the trigger is fully pressed
B6 = Z
B7 = Start
B8 = Dpad Up (mapped as padUp)
B9 = Dpad Down (mapped as padDown)
B10 = Dpad Left (mapped as padLeft)
B11 = Dpad Right (mapped as padRight)
AXIS 0 = leftAxisX (mapped as leftStickLeft and leftStickRight) // -1 = left, 1 = right
AXIS 1 = leftAxisY (mapped as leftStickUp and leftStickDown) // -1 = up, 1 = down
AXIX 2 = LT // reports LT pressed value between -1 (not pressed) and 1 (fully pressed)
AXIS 3 = rightAxisX // -1 = left, 1 = right
AXIS 4 = rightAxisY (mapped as rightStickUp and rightStickDown) // -1 = up, 1 = down
AXIX 5 = RT // reports RT pressed value between -1 (not pressed) and 1 (fully pressed)
```

## Adding layouts

Layouts are defined in the `src/helper/gamepad.ts` file. For a layout definition we need the following information from https://gamepad-tester.com and some additional info:

- Controller ID: name of the controller as reported by the browser
- A list of all the `BX` and `AXIS X` elements and the corresponding button/stick/trigger in the real controller
- Operating System you are using
- If the gamepad is connected wireless or via USB
- You should specify which buttons should map to the valid interactions (mainAction, back, etc)
- Is the controller a clone of another one? (Like it's an alternative PS3 or Xbox controller?)

Layouts can be added to that file by defining a new function the `checkActionsForXbox` and `checkActionsForPlaystation` function or a new issue can be created with all the required information and we can add that.

If the layout corresponds to one of the already defined layouts, report that specifying the controller ID as shown in https://gamepad-tester.com
