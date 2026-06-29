# Tutorial - Part 3: Forcing A Roundtrip

Tutorial - Part 2: Enumerating Objects | Index | Tutorial - Part 4: Playing A Tone

In this tutorial we show how to force a roundtrip to the server
to make sure an action completed.

We'll change our example from Tutorial 2 slightly
and add the extra code to implement the roundtrip.

Let's take the following small method first:

 tutorial3.c roundtrip

Let's take a look at what this method does.

```c
	struct spa_hook core_listener;

	pw_core_add_listener(core, &core_listener, &core_events, &d);
```

First of all we add a listener for the events of the core
object. We are only interested in the `done` event in this
tutorial. This is the event handler:

```c
static void on_core_done(void *data, uint32_t id, int seq)
{
	struct roundtrip_data *d = data;

	if (id == PW_ID_CORE && seq == d->pending)
		pw_main_loop_quit(d->loop);
}
```

When the done event is received for an object with id `PW_ID_CORE` and
a certain sequence number `seq`, this function will call `pw_main_loop_quit()`.

Next we do:

```c
	d.pending = pw_core_sync(core, PW_ID_CORE, 0);
```

This triggers the `sync` method on the core object with id
`PW_ID_CORE` and sequence number 0.

Because this is a method on a proxy object, it will be executed
asynchronously and the return value will reflect this. PipeWire
uses the return values of the underlying SPA (Simple Plugin API)
helper objects (See also SPA Design ).

Because all messages on the PipeWire server are handled sequentially,
the sync method will be executed after all previous methods are
completed. The PipeWire server will emit a `done` event with the
same ID and the return value of the original `pw_core_sync()`
method in the sequence number.

We then run the mainloop to send the messages to the server and
receive the events:

```c
	pw_main_loop_run(loop);
```

When we get the done event, we can compare it to the sync method
and then we know that we did a complete roundtrip and there are no
more pending methods on the server. We can quit the mainloop and
remove the listener:

```c
	spa_hook_remove(&core_listener);
```

If we add this roundtrip method to our code and call it instead of the
`pw_main_loop_run()` we will exit the program after all previous methods
are finished. This means that the `pw_core_get_registry()` call
completed and thus that we also received all events for the globals
on the server.

 tutorial3.c code

To compile the simple test application, copy it into a tutorial3.c file and
use:

	gcc -Wall tutorial3.c -o tutorial3 $(pkg-config --cflags --libs libpipewire-0.3)

Now that our program completes, we can take a look at how we can destroy
the objects we created. Let's destroy each of them in reverse order that we
created them:

```c
	pw_proxy_destroy((struct pw_proxy*)registry);
```

The registry is a proxy and can be destroyed with the generic proxy destroy
method. After destroying the object, you should not use it anymore. It is
an error to destroy an object more than once.

We can disconnect from the server with:

```c
	pw_core_disconnect(core);
```

This will also destroy the core proxy object and will remove the proxies
that might have been created on this connection.

We can finally destroy our context and mainloop to conclude this tutorial:

```c
	pw_context_destroy(context);
	pw_main_loop_destroy(loop);
```

Tutorial - Part 2: Enumerating Objects | Index | Tutorial - Part 4: Playing A Tone
