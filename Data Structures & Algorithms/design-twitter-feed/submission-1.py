import heapq as hq
class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId in self.tweets:
            self.tweets[userId].append((self.time, tweetId))
        else:
            self.tweets[userId] = [(self.time, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        tweetHeap = []
        recentTweets = []
        if userId in self.following:
            people = self.following[userId] | {userId}
        else:
            people = {userId}
        hq.heapify(tweetHeap)
        for followee in people:
            if followee in self.tweets and len(self.tweets[followee]) > 0:
                latest = self.tweets[followee][len(self.tweets[followee])-1]
                hq.heappush(tweetHeap, (-latest[0], latest[1], followee, len(self.tweets[followee])-1))
        
        i = 0
        while i < 10 and tweetHeap:
            tweet = hq.heappop(tweetHeap)
            idx = tweet[3] - 1
            recentTweets.append(tweet[1])
            if idx >= 0:
                latest = self.tweets[tweet[2]][idx]
                hq.heappush(tweetHeap, (-latest[0], latest[1], tweet[2], idx))
            
            i += 1
        
        return recentTweets


            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = {followeeId}
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
