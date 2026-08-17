# System Design Interview Guide

## Table of Contents

1. Introduction
2. Scalability Fundamentals
3. Load Balancing
4. Caching Strategies
5. Database Design
6. API Design
7. Microservices Architecture
8. Message Queues & Event-Driven Systems
9. CAP Theorem & Consistency Models
10. Availability & Reliability
11. System Design Interview Framework
12. Practice Problems
13. Interview Tips
14. Additional Resources

---

## 1. Introduction

System design interviews evaluate your ability to design large-scale distributed systems.

These interviews assess:

- Your understanding of fundamental concepts
- Your problem-solving approach
- Your ability to make trade-offs
- Your communication skills

### Key Principles

- **Think Big:** Design for millions of users
- **Trade-offs:** Every decision has pros and cons
- **Iterative Approach:** Start simple, then scale
- **Communication:** Explain your thinking clearly

---

## 2. Scalability Fundamentals

### Vertical vs Horizontal Scaling

| Aspect     | Vertical Scaling                         | Horizontal Scaling                          |
| ---------- | ---------------------------------------- | ------------------------------------------- |
| Definition | Add more power to existing machine       | Add more machines to the pool               |
| Example    | Upgrade CPU, RAM, Storage                | Add more servers behind load balancer       |
| Pros       | Simple, no code changes                  | Unlimited scaling, fault tolerance          |
| Cons       | Hardware limits, single point of failure | Complex, requires distributed system design |
| Cost       | Expensive at high end                    | Linear cost scaling                         |

**When to Use Each:**

- **Vertical:** Small applications, legacy systems, database primary nodes
- **Horizontal:** Web servers, stateless services, high-traffic applications

---

## 3. Load Balancing

### What is a Load Balancer?

A load balancer distributes incoming network traffic across multiple servers to ensure no single server bears too much demand.

### Load Balancing Algorithms

| Algorithm            | Pros                                           | Cons                                               |
| -------------------- | ---------------------------------------------- | -------------------------------------------------- |
| Round Robin          | Simple, fair distribution                      | Ignores server load, not optimal for varying sizes |
| Least Connections    | Optimizes for current load                     | Overhead of tracking connections                   |
| IP Hash              | Session persistence (same user → same server) | Uneven distribution if IPs are skewed              |
| Weighted Round Robin | Accounts for different server capacities       | Requires manual weight configuration               |

### Load Balancer Types

- **Layer 4 (Transport):** Works on TCP/UDP, faster but less intelligent
- **Layer 7 (Application):** Works on HTTP/HTTPS, can make routing decisions based on content

---

## 4. Caching Strategies

### Why Cache?

- Reduce latency
- Decrease database load
- Improve throughput
- Reduce costs

### Caching Patterns

#### 1. Cache-Aside (Lazy Loading)

```python
def get_data(key):
    data = cache.get(key)
    if data is None:
        data = db.query(key)
        cache.set(key, data)
    return data

Pros: Only caches requested data, simple
Cons: Cache miss penalty, stale data possible
2. Write-Through
python

def write_data(key, value):
    cache.set(key, value)
    db.write(key, value)

Pros: Data always fresh in cache, no cache miss on reads
Cons: Higher write latency, caches all data (even unused)
3. Write-Behind (Write-Back)
python

def write_data(key, value):
    cache.set(key, value)
    # Async batch write to DB
    queue.push(db_write, key, value)

Pros: Fast writes, batch database updates
Cons: Risk of data loss if cache fails before DB write
4. Refresh-Ahead
python

def get_data(key):
    if cache.ttl(key) < threshold:
        cache.async_refresh(key)
    return cache.get(key)

Pros: No cache misses for hot data
Cons: Complex, may cache unused data
Cache Eviction Policies
Policy	Description	Use Case
LRU	Remove least recently accessed	General purpose
LFU	Remove least frequently accessed	Hot data identification
FIFO	Remove oldest entry	Simple queues
TTL	Expire after fixed time	Time-sensitive data
Popular Caching Solutions

    Redis: In-memory, supports complex data structures

    Memcached: Simple, high-performance key-value store

    CDN (CloudFlare, CloudFront): Cache static content at edge locations

5. Database Design
SQL vs NoSQL
Feature	SQL (Relational)	NoSQL
Data Model	Tables with rows/columns	Documents, Key-Value, Graph, Column-family
Schema	Fixed, predefined	Dynamic, flexible
Scaling	Vertical (mostly)	Horizontal (native)
Transactions	ACID compliant	BASE (Basically Available, Soft state, Eventual consistency)
Use Cases	Financial systems, complex queries	Content management, real-time analytics, IoT
Examples	PostgreSQL, MySQL, Oracle	MongoDB, Cassandra, Redis, DynamoDB
Database Sharding

Sharding splits a database into smaller, faster, more easily managed parts called shards.

Sharding Strategies:

    Horizontal Sharding (Range-based)
    user_id 0-1000 → shard_1, 1001-2000 → shard_2
    Pros: Simple to implement
    Cons: Uneven distribution (hotspots)

    Hash-based Sharding
    shard_id = hash(user_id) % num_shards
    Pros: Even distribution
    Cons: Difficult to add/remove shards

    Directory-based Sharding
    Lookup table maps user_id → shard_id
    Pros: Flexible, easy to rebalance
    Cons: Single point of failure (lookup table)

    Geo-based Sharding
    EU users → EU shard, US users → US shard
    Pros: Low latency for regional users, compliance
    Cons: Complex global queries

Database Replication

Master-Slave Replication:

    Writes go to master

    Reads served by slaves

    Pros: Read scaling, backup

    Cons: Single point of failure (master), replication lag

Master-Master Replication:

    Writes can go to any master

    Pros: High availability, no single point of failure

    Cons: Conflict resolution complexity

Indexing Strategies

    B-Tree: Default for most databases, good for range queries

    Hash Index: O(1) lookups, exact matches only

    Bitmap Index: Good for low-cardinality columns (gender, status)

    Covering Index: Includes all columns needed for a query

6. API Design
REST vs GraphQL
Feature	REST	GraphQL
Endpoints	Multiple (/users, /posts, /comments)	Single (/graphql)
Data Fetching	Fixed structure per endpoint	Client specifies exactly what they need
Over-fetching	Common (gets more data than needed)	None (only requested fields)
Under-fetching	Common (needs multiple requests)	None (single request for related data)
Caching	Easy (HTTP caching)	Complex (requires custom solution)
Learning Curve	Low	Medium-High
REST Best Practices

    Use nouns, not verbs: /users, not /getUsers

    Use HTTP methods correctly: GET, POST, PUT, DELETE

    Version your API: /v1/users

    Use proper status codes: 200, 201, 400, 401, 404, 500

    Paginate large responses: ?limit=50&offset=100

    Rate limit requests to prevent abuse

Rate Limiting
Token Bucket Algorithm
python

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.now()

    def allow_request(self):
        self._refill()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

    def _refill(self):
        now = time.now()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now

Implementation Strategies:

    Per User: Track by user ID (requires authentication)

    Per IP: Track by IP address (easier, but less precise)

    Sliding Window: More accurate than fixed windows

7. Microservices Architecture
Monolith vs Microservices
Aspect	Monolith	Microservices
Deployment	Single unit	Independent services
Scaling	Scale entire app	Scale individual services
Technology	Single stack	Polyglot (different stacks per service)
Fault Isolation	One bug can crash everything	Faults isolated to single service
Development	Coordinated releases	Independent teams, faster iteration
Complexity	Lower operational complexity	Higher (network, monitoring, deployment)
Service Decomposition Strategies

    By Business Capability
    User Service, Order Service, Payment Service

    By Subdomain (DDD)
    Domain-Driven Design bounded contexts

    By Data Requirements
    Services that use same data together

Inter-Service Communication

Synchronous (HTTP/RPC):
text

Service A → Service B → Service C

Pros: Simple, immediate response
Cons: Coupling, cascading failures

Asynchronous (Message Queue):
text

Service A → Message Queue → Service B

Pros: Decoupling, fault tolerance, scalability
Cons: Complexity, eventual consistency
API Gateway Pattern
text

Client → API Gateway → Service A
                     → Service B
                     → Service C

Responsibilities:

    Authentication/Authorization

    Rate limiting

    Request routing

    Response aggregation

    Logging/Monitoring

8. Message Queues & Event-Driven Systems
When to Use Message Queues

    Asynchronous processing

    Load leveling (smooth traffic spikes)

    Decoupling services

    Retry mechanisms

    Event broadcasting

Popular Message Brokers
Broker	Type	Use Case
RabbitMQ	Traditional queue	Complex routing, reliability
Kafka	Event streaming	High throughput, event sourcing
AWS SQS	Managed queue	AWS ecosystem, simplicity
Redis Pub/Sub	Pub/Sub	Real-time messaging, chat
Event-Driven Architecture Patterns
1. Event Notification
text

Order Service → "OrderCreated" event → Notification Service

2. Event-Carried State Transfer
text

Order Service → event with full order data → Analytics Service

3. Event Sourcing
text

Store all events, reconstruct current state by replaying events

9. CAP Theorem & Consistency Models
CAP Theorem

In a distributed system, you can only guarantee 2 out of 3:

    Consistency: All nodes see the same data at the same time

    Availability: Every request receives a response (success or failure)

    Partition Tolerance: System continues despite network failures

text

      C
     / \
    /   \
   /     \
  P-------A

Reality: In distributed systems, network partitions are inevitable, so you must choose between CP and AP.
Consistency Models

    Strong Consistency: All reads return latest write
    Use Case: Banking, financial transactions
    Trade-off: Higher latency, lower availability during partitions

    Eventual Consistency: Reads may return stale data temporarily
    Use Case: Social media likes, comments, shopping carts
    Trade-off: May read stale data temporarily

    Causal Consistency: Preserves causal relationships
    Use Case: Comment threads, chat applications

10. Availability & Reliability
Measuring Availability
text

Availability = (Total time - Downtime) / Total time

99% = 3.65 days downtime/year
99.9% = 8.76 hours downtime/year
99.99% = 52.6 minutes downtime/year
99.999% = 5.26 minutes downtime/year

Redundancy Patterns

Active-Active:

    All instances serve traffic

    Pros: No failover delay, better resource utilization

    Cons: Complex data synchronization

Active-Passive:

    One instance serves traffic, other is standby

    Pros: Simpler, no data conflicts

    Cons: Wasted resources, failover delay

Failover Strategies

    Automatic Failover: Health checks detect failure, redirect traffic automatically

    Manual Failover: Human intervention required (safer but slower)

Retry Patterns
python

def retry_with_backoff(func, max_retries=5):
    delay = 1
    for attempt in range(max_retries):
        try:
            return func()
        except Exception:
            if attempt == max_retries - 1:
                raise
            time.sleep(delay)
            delay *= 2  # Exponential backoff

Circuit Breaker Pattern
python

class CircuitBreaker:
    def __init__(self, failure_threshold=5, reset_timeout=60):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.state = "CLOSED"
        self.last_failure_time = None

    def call(self, func):
        if self.state == "OPEN":
            if time.now() - self.last_failure_time > self.reset_timeout:
                self.state = "HALF_OPEN"
            else:
                raise CircuitOpenError()

        try:
            result = func()
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.now()
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e

11. System Design Interview Framework
4-Step Approach
Step 1: Requirements Clarification (5-10 minutes)

Ask questions to understand scope:

    Functional Requirements: What should the system do?

    Non-Functional Requirements: Performance, scalability, availability

    Constraints: Timeline, budget, team size

    Scale: DAU (Daily Active Users), MAU, peak QPS

Example questions:

    How many daily active users?

    What's the read/write ratio?

    Do we need strong consistency or is eventual consistency okay?

    What's the expected latency requirement?

Step 2: High-Level Design (10-15 minutes)

Draw the backbone of your system:
text

Client → Load Balancer → Services → Database

    Identify major components

    Show data flow

    Mention key technologies

Step 3: Deep Dive (15-20 minutes)

Focus on 2-3 critical components:

    Database schema design

    Caching strategy

    Scaling approach

    Handling bottlenecks

Step 4: Wrap-up (5 minutes)

    Identify bottlenecks

    Discuss trade-offs made

    Mention monitoring/logging

    Suggest future improvements

12. Practice Problems
Problem 1: URL Shortener (TinyURL)

Requirements:

    Shorten long URLs (e.g., tinyurl.com/abc123)

    Redirect short URLs to original

    Custom aliases (optional)

    Analytics (click count)

    Expiration (optional)

Scale Estimates:

    100M new URLs/month

    10B redirects/month (100:1 read/write ratio)

    URL storage: ~500 bytes per URL

Design:
text

Client → API Gateway → URL Shortener Service → Cache (Redis)
                                              → Database (DynamoDB)

Key Decisions:

    Short URL Generation: MD5 hash + Base62 encoding, Distributed ID generator (Snowflake), Pre-generate short codes

    Database Choice: NoSQL (DynamoDB) for horizontal scaling, Key: short_url, Value: long_url + metadata

    Caching: Cache popular URLs (LRU), Cache-aside pattern

    Analytics: Async queue to update click counts, Batch writes to reduce DB load

Problem 2: Chat Application (WhatsApp)

Requirements:

    1-on-1 messaging

    Group chats

    Online/offline status

    Message delivery receipts

    Media sharing (images, videos)

    Message history

Scale Estimates:

    500M DAU

    10B messages/day

    Average message size: 1KB

Design:
text

Client ↔ WebSocket Gateway ↔ Message Service ↔ Cassandra
                                     ↕
                                 Redis (presence)

Key Decisions:

    Real-time Communication: WebSocket for persistent connection, Long polling as fallback

    Message Storage: Cassandra for write-heavy workload, Partition by user_id or conversation_id

    Online Status: Redis with TTL (auto-expire when heartbeat stops)

    Message Delivery: Acknowledgment system, Retry with exponential backoff

    Media Storage: Upload to S3, store URL in database, CDN for fast delivery

Problem 3: Video Streaming (YouTube)

Requirements:

    Upload videos

    Transcode to multiple resolutions

    Stream videos (adaptive bitrate)

    Recommendations

    Comments, likes, subscriptions

Scale Estimates:

    2B+ users

    500 hours of video uploaded/minute

    1B+ hours watched/day

Design:
text

Upload → Processing Pipeline → Transcoded Videos → S3 → CDN
Metadata → Database
Watch History → Recommendation Engine

Key Decisions:

    Video Processing: Async transcoding pipeline, Multiple resolutions (360p, 720p, 1080p, 4K), HLS/DASH for adaptive streaming

    Storage: Object storage (S3) for videos, Separate DB for metadata

    Delivery: CDN for global low-latency, Edge caching

    Recommendations: ML model (collaborative filtering, content-based), Pre-compute recommendations, cache results

Problem 4: Ride-Sharing (Uber)

Requirements:

    Request ride

    Match with nearby drivers

    Real-time tracking

    Pricing (surge pricing)

    Payment processing

    Rating system

Scale Estimates:

    10M rides/day

    1M concurrent drivers

    Location updates every 5 seconds

Design:
text

Rider App → Ride Service → Matching Engine → Driver App
                     ↕
                Redis Geo (location)

Key Decisions:

    Location Tracking: Redis Geo (geospatial indexing), Update driver location every 5 seconds, Query: Find drivers within 5km radius

    Ride Matching: Filter by proximity, availability, rating, Priority queue for ride requests

    Surge Pricing: Real-time supply/demand calculation, Geographic zones

    Real-time Updates: WebSocket for live tracking, Push notifications for ride status

Problem 5: Social Media Feed (Twitter)

Requirements:

    Post tweets

    Follow/unfollow users

    Home timeline (feed)

    Notifications

    Trending topics

Scale Estimates:

    300M DAU

    500M tweets/day

    90% read, 10% write

Design Options:
Option 1: Pull Model (Fan-out on Load)
text

User requests feed → Query all followed users → Merge posts

Pros: Simple, storage efficient
Cons: Slow for users following many people
Option 2: Push Model (Fan-out on Write)
text

User posts → Push to all followers' timeline caches

Pros: Fast read experience
Cons: Expensive for celebrities (millions of followers)
Option 3: Hybrid Approach (Recommended)
text

Normal users: Push model (fan-out on write)
Celebrities: Pull model (fan-out on load)

Storage:

    Tweets: Cassandra (write-optimized)

    User relationships: Neo4j or Redis

    Timeline cache: Redis (sorted sets)

Problem 6: E-commerce (Amazon)

Requirements:

    Product catalog

    Search functionality

    Shopping cart

    Order processing

    Payment

    Recommendations

    Inventory management

Scale Estimates:

    300M+ products

    100M DAU

    Peak: 10K orders/second (Black Friday)

Design:
text

Web → API Gateway → Product Service → Catalog DB (NoSQL)
                       → Search Service → Elasticsearch
                       → Cart Service → Redis
                       → Order Service → Order DB
                       → Inventory Service → Event Bus

Key Decisions:

    Product Catalog: NoSQL for flexible schema, CDN for product images

    Search: Elasticsearch for full-text search, Filters, facets, autocomplete

    Shopping Cart: Redis for fast access, Persistent to DB for recovery

    Order Processing: Saga pattern for distributed transactions, Event-driven inventory updates

    Recommendations: Collaborative filtering, Real-time personalization

Problem 7: Web Crawler

Requirements:

    Crawl billions of web pages

    Respect robots.txt

    Politeness (rate limiting per domain)

    Duplicate detection

    Freshness (re-crawl periodically)

Scale Estimates:

    100B+ pages to crawl

    1M pages/second throughput

    Petabytes of storage

Design:
text

URL Frontier → Crawler Workers → Downloader → Content Processor
                     ↑                              ↓
               URL Queue                      Storage (HDFS)

Key Decisions:

    URL Frontier: Priority queue (PageRank, freshness), Per-domain queues for politeness

    Duplicate Detection: Bloom filter for URL deduplication, Simhash for content deduplication

    Politeness: Rate limit per domain (e.g., 1 request/second), Respect robots.txt rules

    Storage: Distributed file system (HDFS), Columnar storage for analytics

    Scalability: Stateless crawler workers, Sharded URL frontier

Problem 8: Rate Limiter

Requirements:

    Limit requests per user/IP/API key

    Configurable limits (e.g., 100 req/min)

    Distributed (work across multiple servers)

    Low latency (<10ms)

Design Options:
Token Bucket (Distributed)
text

Redis: INCR + EXPIRE, Lua script for atomicity

Sliding Window Log
text

Redis sorted set: add timestamp, remove old entries, count remaining

Implementation:
python

def rate_limit(key, limit, window_seconds):
    now = time.now()
    window_start = now - window_seconds
    # Remove old entries
    redis.zremrangebyscore(key, 0, window_start)
    # Count current requests
    current = redis.zcard(key)
    if current >= limit:
        return False
    # Add current request
    redis.zadd(key, {now: now})
    redis.expire(key, window_seconds)
    return True

Key Decisions:

    Algorithm Choice: Sliding window for accuracy, token bucket for simplicity

    Storage: Redis for speed and atomic operations

    Granularity: Per-user, per-IP, per-endpoint

    Response: Return rate limit headers (X-RateLimit-Limit, X-RateLimit-Remaining)

Problem 9: Notification System

Requirements:

    Multiple channels (email, SMS, push, in-app)

    User preferences (opt-in/opt-out)

    Prioritization (urgent vs promotional)

    Retry failed notifications

    Analytics (delivery rate, open rate)

Scale Estimates:

    100M notifications/day

    Multiple templates per channel

    <5 minute delivery SLA

Design:
text

Notification API → Priority Queue → Notification Worker → Email/SMS/Push/In-App
                                          ↓
                                    Dead Letter Queue (failed)

Key Decisions:

    Queue-Based Architecture: Decouple notification generation from delivery, Handle traffic spikes

    Prioritization: Multiple queues (high, medium, low priority), Process high-priority first

    Retry Logic: Exponential backoff, Dead letter queue for failed notifications

    User Preferences: Cache preferences in Redis, Check before sending

    Templates: Store templates in database, Support localization

13. Interview Tips
Do's ✅

    Ask clarifying questions before designing

    Start with requirements and scale estimates

    Draw diagrams and explain your thinking

    Discuss trade-offs explicitly

    Consider failure scenarios

    Mention monitoring and logging

Don'ts ❌

    Jump straight into details without high-level design

    Ignore scalability or assume infinite resources

    Forget about security considerations

    Design in silence (communicate constantly)

    Stick rigidly to one solution (be flexible)

Red Flags for Interviewers

    Can't estimate scale (users, storage, bandwidth)

    Doesn't consider trade-offs

    Ignores failure scenarios

    Can't explain why they chose a technology

    No discussion of monitoring/metrics

## 14. Additional Resources

### Books

- Designing Data-Intensive Applications by Martin Kleppmann
- System Design Interview by Alex Xu (Vol 1 & 2)
- Building Microservices by Sam Newman

### Online Resources

- GitHub: donnemartin/system-design-primer
- High Scalability Blog (highscalability.com)
- AWS Architecture Center
- Google Cloud Architecture Framework

### Practice Platforms

- LeetCode System Design questions
- Pramp (mock interviews)
- Interviewing.io

---

**End of System Design Interview Guide**
