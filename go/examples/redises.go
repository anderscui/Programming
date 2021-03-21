package main

import (
	"fmt"
	"github.com/garyburd/redigo/redis"
)

var RedisPool *redis.Pool

func main() {
	redisAddress := "localhost"
	RedisPool = &redis.Pool{ //实例化一个连接池
		MaxIdle:     16,  //最初的连接数量
		MaxActive:   0,   //连接池最大连接数量,不确定可以用0（0表示自动定义），按需分配
		IdleTimeout: 300, //连接关闭时间 300秒 （300秒不使用自动关闭）
		Dial: func() (redis.Conn, error) { //要连接的redis数据库
			return redis.Dial("tcp", fmt.Sprintf("%v:6379", redisAddress))
		},
	}

	c := RedisPool.Get()
	defer c.Close()

	c.Do("select", "1")
	resp, _ := redis.Strings(c.Do("SMEMBERS", "email_accounts_2"))
	fmt.Println("got account from email_accounts_2", resp)
}