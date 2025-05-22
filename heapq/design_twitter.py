import heapq
from collections import defaultdict
import time
class Twitter:

    def __init__(self):
        self.user_tweet_map=defaultdict(list)
        self.user_follower_map=defaultdict(set)
        #self.user_follower_post_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.user_tweet_map[userId],(-time.time(),tweetId))
        #self.user_tweet_map[userId]=he_structure

    def getNewsFeed(self, userId: int) -> List[int]:
        get_user_tweet= list(self.user_tweet_map[userId])  # Copy to avoid modifying original heap
        return [tweetId for _ ,tweetId in sorted(get_user_tweet,reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None: 
        self.user_follower_map[followerId].add(followeeId)
        # TODO: 
        # for each_followee in get_follower:
        #     if each_followee != followerId:
        #         get_follower_followers= self.user_follower_map.get(each_followee,[])
        #         self.user_follower_map[followerId].extend(get_follower_followers)
        
        merged_tweets=[]
        for each_followee in self.user_follower_map[followerId] :
            if each_followee in self.user_tweet_map:
                merged_tweets.extend(self.user_tweet_map[each_followee])
        heapq.heapify(merged_tweets)
        self.user_tweet_map[followerId] = merged_tweets

                # follower_heap_obj=self.user_tweet_map[each_followee]
                # follower_heap_obj=self.user_tweet_map[followerId]
                # self.user_tweet_map[followerId]= heapq.heapify(list(heapq.merge(follower_heap_obj,follower_heap_obj)))
                

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follower_map[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(userId,tweetId)
param_2 = obj.getNewsFeed(userId)
obj.follow(followerId,followeeId)
obj.unfollow(followerId,followeeId)