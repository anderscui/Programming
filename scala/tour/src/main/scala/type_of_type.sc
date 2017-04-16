// type aliases
object TypeFun {
  type Whole = Int
  val x: Whole = 5

  type UserInfo = (Int, String)
  val u: UserInfo = new UserInfo(1, "Name")

  type T3[A, B, C] = Tuple3[A, B, C]
  val things = new T3(1, 'a', true)
}

TypeFun.x

// abstract
class User(val name: String)
trait Factory { type A; def create: A}
trait UserFactory extends Factory {
  // or use type parameter
  type A = User
  def create = new User("")
}

