Automagical HTTPS with Docker and Go - Brendan Roy

Automagical HTTPS with Docker and Go - Brendan Roy
https://brendanr.net/blog/go-docker-https/

I’ve been building a lot of webhooks lately, and more often than not, I need serve my applications over HTTPS. A common way of quickly achieving this is by utilising Let’s Encrypt , however it can be a bit fiddly to setup. I’d really like to be able to automate the process entirely, including certificate renewal. I’ve been building my applications using docker, and I’d like to keep the build process and container images as lightweight as possible. Lastly, I’d like to have the entire process as application code, so I can easily change and re-deploy things on the fly. Also, having no ops/shell scripts allows my applications to be portable and easily deployed to many different environments.