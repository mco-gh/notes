Relay - A JavaScript framework for building data-driven React applications

[![](../_resources/7b5d584ecc07ab50ac4a8512f3c326e0.png)Relay](https://facebook.github.io/relay/)

- [Try it out](https://facebook.github.io/relay/prototyping/playground.html)
- [Docs](https://facebook.github.io/relay/docs/getting-started.html)
- [Support](https://facebook.github.io/relay/support.html)
- [GitHub](https://github.com/facebook/relay)

![](../_resources/3ee90e81623fe615b8b63547dd883411.png)

# **Relay**

## A JavaScript framework for building data-driven React applications

[Try It Out](https://facebook.github.io/relay/prototyping/playground.html)[Get Started](https://facebook.github.io/relay/docs/getting-started.html)

### Declarative

Declare the data your components need with GraphQL, Relay determines how and when to fetch your data.

### Colocation

GraphQL is written next to the views that rely on them. Relay aggregates queries into efficient network requests.

### Mutations

Write GraphQL mutations and Relay offers automatic data consistency, optimistic updates, and error handling.

New

## Relay Modern (Release Candidate)

Relay Modern is a new version of Relay designed from the ground up to be easier to use, more extensible and, most of all, able to improve performance on mobile devices. Relay Modern accomplishes this with static queries and ahead-of-time code generation.

Incrementally convert existing Relay apps, or start a new one with Relay Modern.

[Try Relay Modern](https://facebook.github.io/relay/docs/relay-modern.html)

## A simple list

Relay lets each view declare its own data requirements in the form of a **GraphQL query fragment**. Here, each tea in this list of teas declares that it needs a `name` and a `steepingTime` to be able to render. Just like we compose React components to build an app, we **compose query fragments** together to build a single query at the root of the app.

​x
 store { ${Component.getFragment('store')} },

1
class  Tea  extends  React.Component {
2
 render() {
3
 var {name, steepingTime} =  this.props.tea;
4
 return (
5
 <li  key={name}>
6
{name} (<em>{steepingTime} min</em>)
7
 </li>
8
);
9
}
10
}
11
Tea  =  Relay.createContainer(Tea, {
12
 fragments: {
13
 tea: () =>  Relay.QL`
14
 fragment on Tea {
15
 name,
16
 steepingTime,
17
 }
18
 `,
19
},
20
});
21
​
22
class  TeaStore  extends  React.Component {
23
 render() {
24
 return  <ul>
25
{this.props.store.teas.map(
26
 tea  =>  <Tea  tea={tea} />
27
)}
28
 </ul>;
29
}
30
}
31
TeaStore  =  Relay.createContainer(TeaStore, {

# Relay Playground

- Earl Grey Blue Star (*5 min*)
- Milk Oolong (*3 min*)
- Gunpowder Golden Temple (*3 min*)
- Assam Hatimara (*5 min*)
- Bancha (*2 min*)
- Ceylon New Vithanakande (*5 min*)
- Golden Tip Yunnan (*5 min*)
- Jasmine Phoenix Pearls (*3 min*)
- Kenya Milima (*5 min*)
- Pu Erh First Grade (*4 min*)
- Sencha Makoto (*2 min*)

## A simple parameterization

Relay query fragments can be parameterized using **variables** in GraphQL **calls**. This enables mechanics like pagination, filtering, sorting, and more.

​x
 game { ${Component.getFragment('game')} },

1
class  Score  extends  React.Component {
2
 render() {
3
 var {initials, score} =  this.props.score;
4
 return (
5
 <li  key={initials}>
6
 <strong>{initials}</strong> {score}
7
 </li>
8
);
9
}
10
}
11
Score  =  Relay.createContainer(Score, {
12
 fragments: {
13
 score: () =>  Relay.QL`
14
 fragment on Score {
15
 initials,
16
 score,
17
 }
18
 `,
19
},
20
});
21
​
22
class  Game  extends  React.Component {
23
 _handleCountChange  = (e) => {
24
 this.props.relay.setVariables({
25
 numToShow: e.target.value
26
 ?  parseInt(e.target.value, 10)
27
: 0,
28
});
29
}
30
 _handleSortChange  = (e) => {
31
 this.props.relay.setVariables({

# Relay Playground

# High Scores

- **N*S**  982523
- **J/D**  982354
- **_LK**  903244
- **FC;**  897252
- **_TY**  897243
- **_JK**  890324
- **Y~Z**  752323
- **#BK**  547840
- **AAA**  348234
- ***DS**  278347

## A simple mutation

Use Relay to change the world through the use of GraphQL mutations. Given a set of **query fragments**, a **mutation**, a query that represents **all parts of the world that might change** as a result of this mutation (the ‘fat query’), and a **set of behaviors to exhibit** when the server responds (the ‘query configs’), Relay will ensure that all of the data necessary to perform the mutation has been fetched, and that your client-side data stays in sync with the server after the mutation.

​x
 ${CreateCommentMutation.getFragment('story')},

1
class  CreateCommentMutation  extends  Relay.Mutation {
2
 static  fragments  = {
3
 story: () =>  Relay.QL`
4
 fragment on Story { id }
5
 `,
6
};
7
 getMutation() {
8
 return  Relay.QL`
9
 mutation{ createComment }
10
 `;
11
}
12
 getFatQuery() {
13
 return  Relay.QL`
14
 fragment on CreateCommentPayload {
15
 story { comments },
16
 }
17
 `;
18
}
19
 getConfigs() {
20
 return [{
21
 type: 'FIELDS_CHANGE',
22
 fieldIDs: { story: this.props.story.id },
23
}];
24
}
25
 getVariables() {
26
 return { text: this.props.text };
27
}
28
}
29
​
30
class  Comment  extends  React.Component {
31
 render() {

# Relay Playground

# Breaking News

The peanut is neither a pea nor a nut.
**Discuss:**

Copyright © 2017 Facebook Inc