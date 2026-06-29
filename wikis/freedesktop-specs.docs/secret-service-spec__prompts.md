## 9 Prompts and Prompting

In order to complete various operations, such as unlocking a collection, the service may need to prompt the user for additional information, such as a master password.

The prompts are displayed by the service on behalf of the client application.

Operations that require a prompt to complete will return a prompt object. The client application must then call the [`Prompt()`](org.freedesktop.Secret.Prompt.md#org.freedesktop.Secret.Prompt.Prompt "org.freedesktop.Secret.Prompt.Prompt") method of the prompt object to display the prompt. Client applications can use the *window-id* argument to display the prompt attached to their application window.

Once the user provides the additional required information to the prompt, the service completes the operation that required the prompt. Then it emits the [`Completed`](org.freedesktop.Secret.Prompt.md#org.freedesktop.Secret.Prompt.Completed "org.freedesktop.Secret.Prompt.Completed") signal of the prompt object. The *result* argument of the signal contains operation an operation specific result.

Either the user or the client application can dismiss a prompt. In this case the operation that required the additional information is cancelled. The client application can dismiss a prompt by calling the [`Dismiss()`](org.freedesktop.Secret.Prompt.md#org.freedesktop.Secret.Prompt.Dismiss "org.freedesktop.Secret.Prompt.Dismiss") method of the prompt object. The `Completed` signal will be emitted with its *dismissed* argument set to `TRUE`.

Once the `Completed` signal is emitted on a prompt object, it is no longer valid. Prompt objects are specific to the client application's connection to the DBus bus. Once an application disconnects, all its prompts are no longer valid.

There is an inherent race between the `Dismiss()` method and the `Completed` signal. An application calling `Dismiss()` must be prepared to handle the fact that the `Completed` has already been emitted (although perhaps not received by the client). In addition the client must be prepared to handle the fact that the prompt object is no longer valid.
