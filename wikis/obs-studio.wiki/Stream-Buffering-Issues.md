Stream buffering can be caused by a number of things, but first and foremost we need to ask the question: Are ***we*** dropping frames? Check the counter at the bottom of the OBS Studio main window:

![Dropped Frame Counter](https://i.imgur.com/ckL3wKb.png)

If this counter is showing dropped frames, the issue is likely with your own connection and you should try our [general connection issue troubleshooting](Dropped-Frames-and-General-Connection-Issues) steps.

Often, you will not drop frames and still have viewers complaining about lag, buffering, or the stream constantly loading. Why is that and what can we do against it? First of all let us take a look at the **why**.

### Why does my stream lag/buffer/load for my viewers?
![Connection Paths](https://i.imgur.com/QWs5gRt.png)

Let's analyze the above picture, which shows two possible scenarios. 
- Provider A has no (or does not always do) balancing of its streams. This means that all streams are served to all viewers from a single server. Twitch.tv for instance, does not use its full Content Delivery Network (CDN) for non-partnered streams. This can lead to very mixed results. User Z can watch your stream just fine, because the route from your Provider to him is very fast or no server on the route is overloaded. But User X might experience problems. He could live in the same country as you, but if the route between him and the provider is too long or is overloaded, he might have problems watching your stream.
- Provider B has different servers all around the world (YouTube, for example) and can send the stream within their own system to their servers. When User Y asks to watch your stream, Provider B will automatically choose the best route (in most cases) to ensure there is no buffering or lag.

There are more ways for your streaming provider to handle the streams, but these two examples are the most commonly used. Provider C might use a combination of both systems, or some form of centralized load balancing other than a CDN.

There's also another simple explanation on why your stream might be buffering:

***YOU USED TOO MUCH BITRATE***

This is a very common mistake that new streamers make. Streamers will tend to use as much bitrate as they have upload available, with no regard to how that might affect their viewers. Of course, we understand you want your stream to look good. Upping your bitrate is a simple way to accomplish that, but it must be within reason. Check the information here provided by Akamai and summarized by OBS forum member RytoEX:

>According to [Akamai's Q4 2016 State of the Internet Connectivity Report](https://www.akamai.com/us/en/multimedia/documents/state-of-the-internet/q4-2016-state-of-the-internet-connectivity-report.pdf), in Q4 2016, 63% of Internet connections in USA were above 10 Mb/s. The average connection speed in USA was 17.2 Mb/s. Average mobile speeds in USA were 5.1 Mb/s. Even mobile users who have access to fast mobile networks would still need to be concerned about bitrate if they are on a data plan with limits and the stream(s) they are watching does not have transcoding.
>
>As bad as that may sound, especially when compared to South Korea or Singapore (or any other nation in the top 10 in any category), connections in much of the rest of the world are still further below those levels (most of the Asia Pacific region - including China and India - most of Europe, all of Africa, all of the Middle East, all of Central America, and all of South America). Russia's average Internet connection speed only clocks in at 11.6 Mb/s with 48% of their connections above 10 Mb/s. Germany's average average Internet connection speed is only 14.6 Mb/s with 50% of their connections above 10 Mb/s.

Basically, this means that just because you can upload 20mb/s constantly without dropping a frame, it does not mean your viewers will be able to download it. Most streaming services impose bitrate limits in part due to this.

In the end while your 1080p 60fps 9mb/s stream might look glorious, and 3 people can watch it fine, either your stream provider or the rest of your viewers very well might have issues. 

And finally...

### What can I do to fix this?
There is unfortunately no perfect cure for this. Let us make it clear once more: **Unless you drop frames, the stream you send out arrived at the server of your provider**. From this point, it is between the provider and your viewers and out of your control.

But we have a few options we can try:
- Lower your bitrate (and if necessary resolution/framerate)
- Try different servers of the same Provider (will probably not help, but especially with Twitch this sometimes can)
- Try a different Provider (might have a better balancing or content distribution)
- Accept that some viewers can encounter problems
- Try again later. The time of day, or the usage amounts of your Provider, can cause your viewers to watch the stream fine one day but not the next.

The Internet is a big amount of highways connected with junctions, at each of the junctions, something can possibly go wrong. We can only make sure to use reasonable bitrate values and not drop frames. Then it is on our providers to do the best they can.