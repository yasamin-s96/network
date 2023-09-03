import Container from "../components/shared/Container"
import Card from "../components/shared/Card"
import { Helmet } from "react-helmet"

const Register = () => {
    return (
        <>
            <Helmet>
                <title>Register</title>
            </Helmet>
            <Container>
                <p className="text-white text-5xl">Join Network Today!</p>
                <Card>
                    <form className="w-full flex flex-col items-center justify-center space-y-3">
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="email" placeholder="Email" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="text" placeholder="Firstname" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="text" placeholder="Lastname" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="text" placeholder="Username" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="password" placeholder="Password" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="password" placeholder="Confirm Password" />
                        <input className="block w-full bg-indigo-300 rounded-lg p-2 text-white hover:cursor-pointer hover:bg-indigo-400" type="submit" value="Sign up" />
                    </form>
                    {/*<already have an account?>*/}

                    {/*<already have an account?/>*/}
                </Card>
            </Container>
        </>

    )
}

export default Register